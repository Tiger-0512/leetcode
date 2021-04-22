from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# DFS with Recursion
class Solution:
    def hasPathSum(self, root: TreeNode, Sum: int) -> bool:
        if not root:
            return

        if not root.left and not root.right and Sum == root.val:
            return True

        return self.hasPathSum(root.left, Sum - root.val) or self.hasPathSum(root.right, Sum - root.val)


#---------------------------------------------------------------------------------------#


# DFS with Stack
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False

        stack = deque()
        stack.append((root, root.val))

        while len(stack) > 0:
            node, currentSum = stack.pop()

            if not node.left and not node.right and currentSum == targetSum:
                return True

            if node.left:
                stack.append((node.left, currentSum + node.left.val))
            if node.right:
                stack.append((node.right, currentSum + node.right.val))

        return False