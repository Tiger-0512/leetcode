# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        # Check input
        if head is None:
            return None

        # Initialization
        slow = head
        fast = head

        while True:
            # Judge the linked list has a cycle
            if fast == None or fast.next == None:
                return None

            # Move pointer
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break

        # Move slow pointer to head
        slow = head

        # Find where the cycle begin
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow