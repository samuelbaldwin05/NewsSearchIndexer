import pytest
from indexer.linkedlist.linklist import LinkedList, Node

@pytest.fixture
def linked_list():
  return LinkedList()


@pytest.fixture
def sample_node():
  return Node("sample", "doc1")


def test_add_node(linked_list):
  linked_list.add("term1", "doc1")
  assert linked_list.head is not None
  assert linked_list.head.term == "term1"
  assert linked_list.head.document_ids == ["doc1"]


def test_add_existing_term(linked_list):
  linked_list.add("term1", "doc1")
  linked_list.add("term1", "doc2")

  assert linked_list.head.term == "term1"
  assert "doc1" in linked_list.head.document_ids
  assert "doc2" in linked_list.head.document_ids


def test_search_existing_node(linked_list):
  linked_list.add("term1", "doc1")
  linked_list.add("term2", "doc2")

  assert linked_list.search("term1") == ["doc1"]
  assert linked_list.search("term2") == ["doc2"]


def test_search_non_existent_node(linked_list, capsys):
  linked_list.add("term1", "doc1")
  linked_list.search("non_existent")

  captured = capsys.readouterr()
  assert "Node not in linked list." in captured.out


def test_remove_existing_node(linked_list):
  linked_list.add("term1", "doc1")
  linked_list.add("term2", "doc2")

  # Remove node with term1
  result = linked_list.remove("term1")
  assert result is True
  assert linked_list.search("term1") is None


def test_remove_non_existent_node(linked_list, capsys):
  linked_list.add("term1", "doc1")
  linked_list.remove("non_existent")

  captured = capsys.readouterr()
  assert "Node not in linked list." in captured.out


def test_node_value_count(sample_node):
  sample_node.add_node("doc2")
  sample_node.add_node("doc3")

  assert sample_node.get_values_count() == 3