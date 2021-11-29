# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:  # If Linked-List is empty, return empty head
            return head
        elif not head.next:  # If Linked-List consist of one element, return empty head
            return head
        else:
            # Keep track of first and second elements, in order to do in-place value change
            previous = head
            current = head.next

            while current:
                a = previous.val  # Keep track of values for exchange
                b = current.val  # Keep track of values for exchange
                previous.val = b  # Exchange the values of 'previous' and 'current'
                current.val = a  # Exchange the values of 'previous' and 'current'

                if previous.next.next and current.next.next:
                    # If there still Nodes to change, then continue
                    previous = previous.next.next
                    current = current.next.next
                else:
                    # If there are no more Nodes, return the Linked-List
                    return head