# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Check input
        if l1 is None and l2 is None:
            return None

        # Initialization
        head = ListNode(0)
        ans = head
        carry = 0

        # Elementary math
        while l1 or l2:
            x = l1.val if l1 is not None else 0
            y = l2.val if l2 is not None else 0
            s = x + y + carry
            ans.next = ListNode(s % 10)
            carry = s // 10
            ans = ans.next

            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
            print(ans)

        if carry > 0:
            ans.next = ListNode(carry)

        return head.next