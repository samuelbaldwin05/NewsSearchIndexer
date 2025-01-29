from typing import List, Optional, Any

from indexer.trees.bst_index import BinarySearchTreeIndex
from indexer.trees.avl_node import AVLNode

class AVLTreeIndex(BinarySearchTreeIndex):
    """
    An AVL Tree implementation of an index that maps a key to a list of values.
    AVLTreeIndex inherits from BinarySearchTreeIndex meaning it automatically
    contains all the data and functionality of BinarySearchTree.  Any
    functions below that have the same name and param list as one in 
    BinarySearchTreeIndex overrides (replaces) the BSTIndex functionality. 

    Methods:
        insert(key: Any, value: Any) -> None:
            Inserts a new node with key and value into the AVL Tree
    """
    
    def __init(self):
       super().__init__()
       self.root: Optional[AVLNode] = None 
    
    def _height(self, node: Optional[AVLNode]) -> int:
        """
        Calculate the height of the given AVLNode.

        Parameters:
        - node: The AVLNode for which to calculate the height.

        Returns:
        - int: The height of the AVLNode. If the node is None, returns 0.
        """
        
        
        if not node:
            return 0
        return node.height

    def _rotate_right(self, y: AVLNode) -> AVLNode:
        """
        Performs a right rotation on the AVL tree.

        Args:
            y (AVLNode): The node to be rotated.

        Returns:
            AVLNode: The new root of the rotated subtree.
        """
        
        x = y.left
        T2 = x.right

        # Perform rotation
        x.right = y
        y.left = T2

        # Update heights
        y.height = 1 + max(self._height(y.left), self._height(y.right))
        x.height = 1 + max(self._height(x.left), self._height(x.right))

        return x

    def _rotate_left(self, x: AVLNode) -> AVLNode:
        """
        Rotate the given node `x` to the left.
        Args:
            x (AVLNode): The node to be rotated.
        Returns:
            AVLNode: The new root of the subtree after rotation.
        """
        
        y = x.right
        T2 = y.left

        # Perform rotation
        y.left = x
        x.right = T2

        # Update heights
        x.height = 1 + max(self._height(x.left), self._height(x.right))
        y.height = 1 + max(self._height(y.left), self._height(y.right))

        return y

    def _insert_recursive(self, current: Optional[AVLNode], key: Any, value: Any) -> AVLNode:
        """
        Recursively inserts a new node with the given key and value into the AVL tree.
        Args:
            current (Optional[AVLNode]): The current node being considered during the recursive insertion.
            key (Any): The key of the new node.
            value (Any): The value of the new node.
        Returns:
            AVLNode: The updated AVL tree with the new node inserted.
        """
        # Perform standard BST insertion (but with AVLNode)
        if current is None:
            new_node = AVLNode(key)
            new_node.add_value(value)
            return new_node
        elif key < current.key:
            current.left = self._insert_recursive(current.left, key, value)
        elif key > current.key:
            current.right = self._insert_recursive(current.right, key, value)
        else:
            # Key exists: append value and return early (no structural changes)
            current.add_value(value)
            return current

        # Update height of current node
        current.height = 1 + max(self._height(current.left), self._height(current.right))

        # Check balance factor and rotate if needed
        balance = self._height(current.left) - self._height(current.right)

        # LL
        if balance > 1 and key < current.left.key:
            return self._rotate_right(current)

        # RR
        if balance < -1 and key > current.right.key:
            return self._rotate_left(current)

        # LR
        if balance > 1 and key > current.left.key:
            current.left = self._rotate_left(current.left)
            return self._rotate_right(current)

        # RL
        if balance < -1 and key < current.right.key:
            current.right = self._rotate_right(current.right)
            return self._rotate_left(current)

        return current

    def insert(self, key: Any, value: Any) -> None:
        """
        Inserts a key-value pair into the AVL tree. If the key exists, the
         value will be appended to the list of values in the node. 

        Parameters:
            key (Any): The key to be inserted.
            value (Any): The value associated with the key.

        Returns:
            None
        """
        if self.root is None:
            self.root = AVLNode(key)
            self.root.add_value(value)
        else:
            self.root = self._insert_recursive(self.root, key, value)

    # def _inorder_traversal(self, current: Optional[AVLNode], result: List[Any]) -> None:
    #     if current is None:
    #         return
        
    #     self._inorder_traversal(current.left, result)
    #     result.append(current.key)
    #     self._inorder_traversal(current.right, result)
   
    # def get_keys(self) -> List[Any]:
    #     keys: List[Any] = [] 
    #     self._inorder_traversal(self.root, keys)
    #     return keys