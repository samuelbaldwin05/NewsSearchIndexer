from ll_node import Node

class LinkedList():
    
    def __init__(self):
        self.head = None

    def add(self, term, document_id):
        # Checking to see if term we are trying to add is in the list
        current = self.head
        while current is not None:
            if current.term == term:
                current.document_ids.add(document_id)
                return
            current = current.next

        # If the node isn't in the list add it to the list
        add = Node(term, document_id)
        add.next = self.head
        self.head = add

    def search(self, term):
        current = self.head
        while current is not None:
            if current.term == term:
                return current.document_ids
            current = current.next
        return print('Node not in linked list.')

    def remove(self, term):
        current = self.head
        prev = None

        while current:
            if current.term == term:
                if prev is None:
                    self.head = current.next
                else:
                    prev.next = current.next
                return True
            prev = current
            current = current.next

        return print('Node not in linked list.')

    def display(self):
        current = self.head
        while current:
            print(f"Term: {current.term}, Document IDs: {current.document_ids}")
            current = current.next
