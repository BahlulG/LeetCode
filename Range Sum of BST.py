# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.answer = 0

        def traverse(node):
            if node:
                if low <= node.val <= high:
                    # If Node Value falls between Lower and Higher inclusive, we will add it to answer
                    self.answer += node.val

                if low < node.val:
                    # If Node Value greater than Lower, move towards to the left Subtree
                    traverse(node.left)

                if high > node.val:
                    # If Node Value lower than Higher, move towards to the right Subtree
                    traverse(node.right)

            return self.answer

        return traverse(root)