import collections

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# O(n) DFS Solution with Recursion
class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if not root1:
            return root2
        if not root2:
            return root1

        root1.val += root2.val
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)

        return root1


#---------------------------------------------------------------------------------------#


# O(n) DFS Solution with Stack
class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if not root1:
            return root2

        stack = collections.deque()
        stack.append((root1, root2))

        while stack:
            n1, n2 = stack.pop()
            if not n1 or not n2:
                continue

            n1.val += n2.val

            if not n1.left:
                n1.left = n2.left
            else:
                stack.append((n1.left, n2.left))

            if not n1.right:
                n1.right = n2.right
            else:
                stack.append((n1.right, n2.right))

        return root1


#---------------------------------------------------------------------------------------#


# O(n) BFS Solution with Queue
class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if not root1:
            return root2
        if not root2:
            return root1

        root1.val += root2.val
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)

        return root1