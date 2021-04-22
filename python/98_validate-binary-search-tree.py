# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# DFS with Recursion
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def recursive(root, low=-float('inf'), high=float('inf')):
            if not root:
                return True

            if low >= root.val or root.val >= high:
                return False
            if not recursive(root.left, low, root.val):
                return False
            if not recursive(root.right, root.val, high):
                return False
            return True

        return recursive(root)


#---------------------------------------------------------------------------------------#


# DFS with Stack
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True

        stack = [(root, -float('inf'), float('inf'))]

        while stack:
            root, low, high = stack.pop()
            if not root:
                continue

            if low >= root.val or root.val >= high:
                print('test')
                return False
            stack.append((root.left, low, root.val))
            stack.append((root.right, root.val, high))

        return True