from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        idxmap = dict()
        for i, n in enumerate(inorder):
            idxmap[n] = i

        preorder_q = deque()
        preorder_q.extend(preorder)

        return self.helper(preorder_q, idxmap, 0, len(preorder))


    def helper(self, preorder, idxmap, l_pointer, r_pointer):
        if l_pointer >= r_pointer:
            return

        num = preorder.popleft()
        root = TreeNode(num)
        idx = idxmap.get(num)

        root.left = self.helper(preorder, idxmap, l_pointer, idx)
        root.right = self.helper(preorder, idxmap, idx + 1, r_pointer)

        return root