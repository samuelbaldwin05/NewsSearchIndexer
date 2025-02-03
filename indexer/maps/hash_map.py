from typing import Any, List

class HashMapIndex():
    def __init__(self, capacity): 
        self.capacity = capacity
        self.table = [None] * capacity 
  
    def _hash(self, term): 
        return hash(term) % self.capacity 
  
    def insert(self, term, document_id):
        index = self._hash(term) 
  
        if self.table[index] is None: 
            self.table[index] = Node(term, document_id) 
        else:
            current = self.table[index] 
            while current: 
                if current.term == term:
                    current.value.append(document_id)
                    return
                current = current.next
            new_node = Node(term, document_id) 
            new_node.next = self.table[index] 
            self.table[index] = new_node 

    def search(self, term): 
        index = self._hash(term) 
  
        current = self.table[index] 
        while current: 
            if current.term == term: 
                return current.value
            current = current.next
  
        return []
  
    def remove(self, term): 
        index = self._hash(term) 
  
        previous = None
        current = self.table[index] 
  
        while current: 
            if current.term == term: 
                if previous: 
                    previous.next = current.next
                else: 
                    self.table[index] = current.next
                return
            previous = current 
            current = current.next

    def get_keys(self) -> List[Any]:
        """
        Returns:
            List[Any]: A list of keys in ascending order.
        """
        keys: List[Any] = []
        for index in range(self.capacity):
            current = self.table[index]
            while current:
                keys.append(current.term)
                current = current.next
        return keys

    def get_unique_values(self) -> int:
        """ Returns number of unique values"""
        unique_values = set()
        for index in range(self.capacity):
            current = self.table[index]
            while current:
                unique_values.add(current.value)
                current = current.next

        return len(unique_values)

class Node: 
    def __init__(self, term, value): 
        self.term = term 
        self.value = [value] 
        self.next = None
