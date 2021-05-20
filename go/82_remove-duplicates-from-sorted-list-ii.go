/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func deleteDuplicates(head *ListNode) *ListNode {
	sentinel := &ListNode{
		Val:  0,
		Next: head,
	}
	predNode := sentinel

	for head != nil {
		if head.Next != nil && head.Val == head.Next.Val {
			for head.Next != nil && head.Val == head.Next.Val {
				head = head.Next
			}
			predNode.Next = head.Next
		} else {
			predNode = predNode.Next
		}
		head = head.Next
	}
	return sentinel.Next
}