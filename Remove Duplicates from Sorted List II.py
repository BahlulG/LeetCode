# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def deleteDuplicates(self, head: ListNode) -> ListNode:
    predecessor = sentinel = ListNode(0, head)
    # sentinel: the first node, before the head
    # predecessor: the last node and/or before the sublist of duplicates

    while head:
        if head.next and head.val == head.next.val:
            # If it's a beginning of duplicates sublist, skip all duplicates
            # and move till the end of duplicates sublist

            while head.next and head.val == head.next.val:
                head = head.next

            predecessor.next = head.next
            # skip all duplicates, point 'predecessor.next' to non-duplicate value

        else:
            # otherwise, move forward predecessor
            predecessor = predecessor.next

        head = head.next
        # If none of above conditions, move forward

    return sentinel.next

# Check the screenshot 'Remove Duplicates from Sorted List II'
