/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
// Iteration
func reverseList(head *ListNode) *ListNode {
	var prev *ListNode
	cur := head

	for cur != nil {
		nextTmp := cur.Next
		cur.Next = prev
		prev = cur
		cur = nextTmp
	}
	return prev
}

/*---------------------------------------------------------------------------------------*/

// Stack
func reverseList(head *ListNode) *ListNode {
	if head == nil {
		return nil
	}

	s := &stack{}
	for head != nil {
		s.push(head)
		head = head.Next
	}

	cur := s.pop()
	head = cur
	for len(s.data) > 0 {
		tmp := &ListNode{Val: s.pop().Val}
		cur.Next = tmp
		cur = cur.Next
	}
	return head
}

type stack struct {
	data []*ListNode
}

func (s *stack) push(node *ListNode) {
	s.data = append(s.data, node)
}
func (s *stack) pop() *ListNode {
	l := len(s.data)
	last := s.data[l-1]
	s.data = s.data[:(l - 1)]
	return last
}