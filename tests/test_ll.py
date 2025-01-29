import pytest
from indexer.linkedlist.linklist import LinkedList
from indexer.linkedlist.ll_node import Node


@pytest.fixture
def linked_list():
  return LinkedList()


@pytest.fixture
def sample_node():
  return Node("sample", "doc1")

