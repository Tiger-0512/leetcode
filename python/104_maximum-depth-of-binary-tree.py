from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# DFS with Recursion
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def dfs(root, d=0, d_max=0):
            if not root:
                return d

            left = dfs(root.left, d + 1, d_max)
            right = dfs(root.right, d + 1, d_max)

            d_max = max(left, right)
            return d_max

        d_max = dfs(root)

        return d_max


#---------------------------------------------------------------------------------------#


# DFS with Stack
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        d_max = 0

        if not root:
            return d_max

        stack = deque()
        stack.append((root, 1))

        while stack:
            root, d = stack.popleft()

            if not root:
                continue

            stack.append((root.left, d + 1))
            stack.append((root.right, d + 1))

            d_max = max(d_max, d)
        return d_max