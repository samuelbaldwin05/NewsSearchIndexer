from indexer.trees.avl_tree import AVLTreeIndex

avl_tree = AVLTreeIndex()

# Insert keys that would unbalance a regular BST
avl_tree.insert(30, "A")
avl_tree.insert(20, "B")
avl_tree.insert(40, "C")
avl_tree.insert(10, "D")
avl_tree.insert(25, "E")
avl_tree.insert(50, "F")

# Check height (should be balanced)
print("Tree Height:", avl_tree.tree_height())