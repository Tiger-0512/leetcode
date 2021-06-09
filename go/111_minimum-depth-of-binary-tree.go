/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

type queue struct {
	node *TreeNode
	l    int
}

func minDepth(root *TreeNode) int {
	if root == nil {
		return 0
	}

	var q []queue
	q = append(q, queue{root, 1})

	for len(q) > 0 {
		node, l := q[0].node, q[0].l
		q = q[1:]

		if node.Left == nil && node.Right == nil {
			return l
		}

		if node.Left != nil {
			q = append(q, queue{node.Left, l + 1})
		}
		if node.Right != nil {
			q = append(q, queue{node.Right, l + 1})
		}
	}
	return -1
}
