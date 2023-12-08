# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Helper function to build a tree from a list
def build_tree(lst, index = 0):
    if index >= len(lst) or lst[index] is None:
        return None
    root = TreeNode(lst[index])
    root.left = build_tree(lst, 2 * index + 1)
    root.right = build_tree(lst, 2 * index + 2)
    return root

