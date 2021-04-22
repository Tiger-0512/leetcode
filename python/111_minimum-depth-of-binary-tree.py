from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# DFS with Recursion
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        return self.recursion(root, 1, float('inf'))

    def recursion(self, root, d, ans):
        if not root:
            return 0
        if not root.left and not root.right:
            return min(d, ans)

        if root.left:
            ans = self.recursion(root.left, d+1, ans)
        if root.right:
            ans = self.recursion(root.right, d+1, ans)

        return ans


#---------------------------------------------------------------------------------------#


# DFS with Stack
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        ans = float('inf')
        stack = deque()
        stack.append((root, 1))

        count = 0
        while len(stack) > 0:
            node, depth = stack.pop()

            if not node.left and not node.right:
                ans = min(ans, depth)
            if node.left:
                stack.append((node.left, depth + 1))
            if node.right:
                stack.append((node.right, depth + 1))

        return ans


#---------------------------------------------------------------------------------------#


# BFS with Queue
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        ans = float('inf')
        queue = deque()
        queue.append((root, 1))

        count = 0
        while len(queue) > 0:
            node, depth = queue.popleft()

            if not node.left and not node.right:
                ans = min(ans, depth)
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))

        return ans