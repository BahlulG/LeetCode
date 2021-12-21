# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def LLtoArray(self, head):
        # Step 1: Go through the Linked-List, append all the Nodes' Value to Array
        array = []

        while head:
            array.append(head.val)
            head = head.next

        return array

    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        # Step 2: Use above created Array to create BST
        values = self.LLtoArray(head)

        def ConvertToBST(left, right):
            if left > right:
                # If Left value goes above Right value, it means cross happened between Left and Right, recursion should stop
                return None

            mid = (left + right) // 2
            node = TreeNode(values[mid])

            if left == right:
                # If Left value equals Right value, it means Left and Right meets, recursion should stop
                return node

            node.left = (ConvertToBST(left, mid - 1))
            node.right = (ConvertToBST(mid + 1, right))
            return node

        return ConvertToBST(0, len(values) - 1)