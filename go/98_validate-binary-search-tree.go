/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func isValidBST(root *TreeNode) bool {
	return recursion(root, nil, nil)
}

func recursion(node *TreeNode, floor *int, ceil *int) bool {
	if node == nil {
		return true
	}
	if floor != nil && node.Val <= *floor {
		return false
	}
	if ceil != nil && node.Val >= *ceil {
		return false
	}
	return recursion(node.Left, floor, &node.Val) && recursion(node.Right, &node.Val, ceil)
}