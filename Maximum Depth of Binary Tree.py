# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        leftDepth = self.maxDepth(root.left)
        rightDepth = self.maxDepth(root.right)

        
        # Recursive call left and right subtree, will go until the Node is None
        # Then, the last recursion's return value will be equal to 1. In last call, either left or right Node will exist.
        # Everytime recursion 'return' will add +1 to the maximum value. In our case, maximum value out of left or right will be one of them.
        # Every recursion 'return' will add +1 to the maximum value.
        return max(leftDepth, rightDepth) + 1
