

  
class HashMapIndex(): 
    def __init__(self, capacity): 
        self.capacity = capacity
        self.table = [None] * capacity 
  
    def _hash(self, term): 
        return hash(term) % self.capacity 
  
    def add(self, term, document_id): 
        index = self._hash(term) 
  
        if self.table[index] is None: 
            self.table[index] = Node(term, document_id) 
        else:
            current = self.table[index] 
            while current: 
                if current.term == term: 
                    if document_id not in current.value:
                        current.value.append(document_id) 
                        return
                    else:
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
                return (current.value)
            current = current.next
  
        raise KeyError(term) 
  
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
 
class Node: 
    def __init__(self, term, value): 
        self.term = term 
        self.value = [value] 
        self.next = None
