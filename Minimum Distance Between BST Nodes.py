# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        stack = []

        def TraverseInorder(node):
            # In-Order traversal will append Tree Node Values to the array in sorted format
            if node:
                TraverseInorder(node.left)
                stack.append(node.val)
                TraverseInorder(node.right)

        TraverseInorder(root)
        minimum = math.inf
        # Here we make minimum to have some infinite value (Read about math.inf)

        while len(stack) > 1:
            temp = abs(stack.pop(0) - stack[0])
            # Here we pop the first element of the stack, then compare the difference with next value
            if temp < minimum:
                # If output is lower the value of minimum:

                minimum = temp
                # Then we assign temp value to minimum

        return minimum