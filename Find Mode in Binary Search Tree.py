# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        dictionary = {}
        answer = []

        def traverse(node):
            if node:
                if node.val not in dictionary:
                    dictionary[node.val] = 1
                    # If Node value doesn't exist in dictionary, add Node Value as Key, 1 as Value

                else:
                    dictionary[node.val] += 1
                    # If Node value exists in dictionary, increase the Value of Node Value's Key, by 1

                return (traverse(node.right)) or (traverse(node.left))
                # Repeat the above steps for Left and Right subtree of the Root Node

        traverse(root)

        maximum = max(dictionary.values())
        # Find the Maximum number among the Dictionary Values

        for key, value in dictionary.items():
            if value == maximum:
                # If the above Dictionary Value equals to Maximum number:

                answer.append(key)
                # Append the Key of Maximum Value to the Answer array

        return answer
