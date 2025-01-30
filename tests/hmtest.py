import pytest
from indexer.maps.hash_map import HashMapIndex

@pytest.fixture
def htable():
    return HashMapIndex(131)

def test_insert_single_node(htable):
    htable.add("a", "file1.json")
    assert htable.search("a") == ["file1.json"]

def test_insert_multiple_nodes(htable):
    htable.add("a", "file1.json")
    htable.add("b", "file2.json")
    htable.add("c", "file3.json")

    assert htable.search("a") == ["file1.json"]
    assert htable.search("b") == ["file2.json"]
    assert htable.search("c") == ["file3.json"]

def test_for_dupes(htable):
    htable.add("a", "file1.json")
    htable.add("a", "file1.json")
    htable.add("a", "file1.json")

    assert htable.search("a") == ["file1.json"]
def test_for_error(htable):
    htable.add("3", "fornhite.json")


    assert htable.search("a") == KeyError("a")

def test_remove(htable):
    htable.add("a", "file1.json")
    assert htable.search("a") == ["file1.json"]
    htable.remove("a")
    try:
        htable.search("a")
    except:
        pass

