# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        sentinel = ListNode(0, head)
        pred = sentinel
        curr = sentinel

        while curr:
            while curr.next and curr.val == curr.next.val:
                curr = curr.next
            if pred.next == curr:
                pred = pred.next
                curr = curr.next
            else:
                curr = curr.next
                pred.next = curr  # Update pred.next, but do not update pred

        return sentinel.next