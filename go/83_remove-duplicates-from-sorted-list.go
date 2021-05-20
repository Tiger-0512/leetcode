/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func deleteDuplicates(head *ListNode) *ListNode {
	curNode := head
	for curNode != nil && curNode.Next != nil {
		for curNode.Next != nil && curNode.Val == curNode.Next.Val {
			curNode.Next = curNode.Next.Next
		}
		curNode = cur.Next
	}
	return head
}