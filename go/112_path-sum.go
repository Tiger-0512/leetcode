/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

// DFS with Recursion
func hasPathSum(root *TreeNode, targetSum int) bool {
	if root == nil {
		return false
	}

	if root.Left == nil && root.Right == nil {
		return root.Val == targetSum
	}

	return hasPathSum(root.Left, targetSum-root.Val) || hasPathSum(root.Right, targetSum-root.Val)
}

/*---------------------------------------------------------------------------------------*/

// BFS with Queue
type queue struct {
	node *TreeNode
	sum  int
}

func hasPathSum(root *TreeNode, targetSum int) bool {
	if root == nil {
		return false
	}

	var q []queue
	q = append(q, queue{root, root.Val})

	for len(q) > 0 {
		node, sum := q[0].node, q[0].sum
		q = q[1:]

		if node.Left == nil && node.Right == nil {
			if sum == targetSum {
				return true
			}
		}

		if node.Left != nil {
			q = append(q, queue{node.Left, sum + node.Left.Val})
		}
		if node.Right != nil {
			q = append(q, queue{node.Right, sum + node.Right.Val})
		}
	}
	return false
}