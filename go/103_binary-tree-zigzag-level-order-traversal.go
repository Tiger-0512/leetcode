/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

type queue struct {
	n *TreeNode
	l int
}

func zigzagLevelOrder(root *TreeNode) [][]int {
	if root == nil {
		return nil
	}

	var out [][]int
	var ans [][]int

	var q []queue
	q = append(q, queue{root, 0})

	for len(q) > 0 {
		node, l := q[0].n, q[0].l
		q = q[1:]

		if node != nil {
			if len(out) <= l {
				out = append(out, []int{})
			}
			out[l] = append(out[l], node.Val)

			q = append(q, queue{node.Left, l + 1})
			q = append(q, queue{node.Right, l + 1})
		}
	}

	for i := 0; i < len(out); i++ {
		if i%2 == 0 {
			ans = append(ans, out[i])
		} else {
			ans = append(ans, reverse(out[i]))
		}
	}
	return ans
}

func reverse(l []int) []int {
	for i := 0; i < len(l)/2; i++ {
		l[i], l[len(l)-i-1] = l[len(l)-i-1], l[i]
	}
	return l
}
