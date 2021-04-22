import queue
from collections import defaultdict

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        out = defaultdict(list)
        l = 0

        if not root:
            return []

        q = queue.Queue()
        q.put((root, l))

        while not q.empty():
            root, l = q.get()

            if not root:
                continue

            out[l].append(root.val)

            q.put((root.left, (l + 1)))
            q.put((root.right, (l + 1)))

        return [out[i] for i in out]