import pytest
from indexer.trees.avl_tree import AVLTreeIndex

@pytest.fixture
def avl_tree():
    return AVLTreeIndex()

def test_insert_single_node(avl_tree):
    avl_tree.insert("a", "file1.json")
    assert avl_tree.search("a") == ["file1.json"]

def test_insert_multiple_nodes(avl_tree):
    avl_tree.insert("a", "file1.json")
    avl_tree.insert("b", "file2.json")
    avl_tree.insert("c", "file3.json")

    assert avl_tree.search("a") == ["file1.json"]
    assert avl_tree.search("b") == ["file2.json"]
    assert avl_tree.search("c") == ["file3.json"]

def test_tree_balance_after_insertions(avl_tree):
    avl_tree.insert("4", "file1.json")
    avl_tree.insert("2", "file2.json")
    avl_tree.insert("5", "file3.json")
    avl_tree.insert("1", "file4.json")  # LL
    avl_tree.insert("3", "file5.json")  # RL

    assert avl_tree.root.key == "4"
    assert avl_tree.root.left.key == "2"
    assert avl_tree.root.right.key == "5"

def test_insert_duplicate_key(avl_tree):
    avl_tree.insert("a", "file1.json")
    avl_tree.insert("a", "file2.json")

    assert avl_tree.search("a") == ["file1.json", "file2.json"]

def test_search_non_existent_key(avl_tree):
    with pytest.raises(KeyError):
        avl_tree.search("nonexistent")

def test_tree_height(avl_tree):
    avl_tree.insert("1", "file1.json")
    avl_tree.insert("2", "file2.json")
    avl_tree.insert("3", "file3.json")
    avl_tree.insert("4", "file4.json")
    avl_tree.insert("5", "file5.json")
    avl_tree.insert("6", "file6.json")
    avl_tree.insert("7", "file7.json")

    height = avl_tree.tree_height()
    assert height <= 3

def test_in_order_traversal(avl_tree):
    avl_tree.insert("a", "file1.json")
    avl_tree.insert("b", "file2.json")
    avl_tree.insert("c", "file3.json")
    avl_tree.insert("d", "file4.json")

    keys_in_order = [node.key for node in avl_tree]
    assert keys_in_order == ["a", "b", "c", "d"]

