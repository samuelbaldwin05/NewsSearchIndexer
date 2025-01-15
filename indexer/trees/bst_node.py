from typing import List, Optional, Any


class BSTNode:
    """
    Binary Search Tree Node.
    Attributes:
        key: The key value of the node.
        values: A list of values associated with the key.
        left: The left child node.
        right: The right child node.
    Methods:
        add_value(value: Any) -> None:
            Adds a value to the list of values associated with the key.
        get_values_count() -> int:
            Returns the number of values associated with the key.
    """
    def __init__(self, key: Any):
        self.key: Any = key
        self.values: List[Any] = []
        self.left: Optional['BSTNode'] = None
        self.right: Optional['BSTNode'] = None
        
    def add_value(self, value: Any) -> None:
        """
        Adds a value to the node.

        Parameters:
            value (Any): The value to be added.

        Returns:
            None
        """
        self.values.append(value)

        
    def get_values_count(self):
        """
        Returns the number of values stored in the node.

        Returns:
            int: The number of values stored in the node.
        """
        return len(self.values)