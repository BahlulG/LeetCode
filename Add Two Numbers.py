# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        else:
            carry = 0
            newHead = tracker = ListNode
            # Keep track of the pointer: 'newHead' will change the pointer to the next Node,
            # each time we will add new Node
            # But, we need the 'Tracker', in order to return the linked-list, from the beginning,
            # at the end of the while loop

            while l1 or l2 or carry:
                # If any of 'l1 or l2 or carry' is true, continue running while loop
                # There can be the situation that 'l1' length is bigger than 'l2', or vice-versa, or we gone through
                # the lists, but we still have some value in 'carry', which we have to add to 'newHead'
                
                if l1:
                    carry += l1.val
                    l1 = l1.next

                if l2:
                    carry += l2.val
                    l2 = l2.next

                newHead.next = ListNode(carry % 10)  # Add remainder to the current Node: 15 % 10 = 5
                carry = carry // 10  # Keep floor division to next Node: 15 // 10 = 1
                newHead = newHead.next  # Move pointer to next 'newHead'

            return tracker.next  # Return new Linked-list from the beginning
