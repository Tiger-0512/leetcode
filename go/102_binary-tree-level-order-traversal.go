/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

// DFS with Recursion
func levelOrder(root *TreeNode) [][]int {
	ans := [][]int{}

	recursion(root, 0, &ans)
	return ans
}

func recursion(node *TreeNode, level int, ans *[][]int) {
	if node == nil {
		return
	}

	if len(*ans) < level+1 {
		*ans = append(*ans, []int{})
	}
	(*ans)[level] = append((*ans)[level], node.Val)
	recursion(node.Left, level+1, ans)
	recursion(node.Right, level+1, ans)
}

// BFS with Queue
func levelOrder(root *TreeNode) [][]int {
	var ans [][]int
	var queue []*TreeNode

	queue = append(queue, root)

	for len(queue) > 0 {
		var curList []int
		n := len(queue)

		for i := 0; i < n; i++ {
			node := queue[0]
			queue = queue[1:]

			if node == nil {
				continue
			}
			curList = append(curList, node.Val)
			queue = append(queue, node.Left)
			queue = append(queue, node.Right)
		}

		if len(curList) > 0 {
			ans = append(ans, curList)
		}
	}

	return ans
}