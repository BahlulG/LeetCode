# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        dic = {}

        def find_min(node):
            if not node:
                # During the recursion, if Root node equals to None, break recursion
                return

            dic[(abs(node.val - target))] = node.val
            # Step 1: Add every 'Node - Target = value' to the dictionary as a key, Node Value as a value

            return (find_min(node.right)) or (find_min(node.left))
            # Repeat the Step 1 for Left and Right Subtree of the Root Node

        find_min(root)
        # Run above created 'find_min' function

        return dic[min(dic.keys())]
        # Return the value of Minimum Value's Key from dictionary
