# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        cur = head
        Max = head

        while cur:
            if cur.val != Max.val:
                Max.next = cur
                Max = cur

            cur = cur.next

        Max.next = None
        return head