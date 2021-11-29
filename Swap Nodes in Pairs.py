# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:  # If Linked-List is empty, return empty head
            return head
        elif not head.next:  # If Linked-List consist of one element, return head
            return head
        else:
            # Keep track of the first and second elements, in order to do in-place value change
            previous = head
            current = head.next

            while current:
                a = previous.val  # Keep track of values for swap
                b = current.val  # Keep track of values for swap
                previous.val = b  # Swap the values of 'previous' and 'current'
                current.val = a  # Swap the values of 'previous' and 'current'

                if previous.next.next and current.next.next:
                    # If there still Nodes to swap the values, then move two Nodes futher
                    previous = previous.next.next
                    current = current.next.next
                else:
                    # If there are no more Nodes to swap the values, return the Linked-List
                    return head
