from indexer.trees.avl_tree import AVLTreeIndex

avl_tree = AVLTreeIndex()

# Insert keys that would unbalance a regular BST
avl_tree.insert(30, ["A", "P"])
avl_tree.insert(20, "B")
avl_tree.insert(40, "C")
avl_tree.insert(10, "D")
avl_tree.insert(25, "E")
avl_tree.insert(50, "F")
avl_tree.insert(70, "j")
avl_tree.insert(34, "q")
avl_tree.insert(52, "r")
avl_tree.insert(9, "z")
avl_tree.insert(9, "e")
avl_tree.insert(8, "p")
avl_tree.insert(8, "l")
avl_tree.insert(7, "m")

# Check height (should be balanced)
print("Tree Height:", avl_tree.tree_height())