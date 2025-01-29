class Node:
    def __init__(self,term,document_id):
        self.term = term
        self.document_ids = [document_id]
        self.next = None
    
    def add_node(self,value):
        self.document_ids.append(value)
        
    def get_values_count(self):
        """
        Returns the number of values stored in the node.

        Returns:
            int: The number of values stored in the node.
        """
        return len(self.document_ids)