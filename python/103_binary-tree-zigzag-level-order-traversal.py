from collections import defaultdict, deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        out = defaultdict(list)
        l = 0
        ans = []

        if not root:
            return []

        d = deque()
        d.append((root, l))

        while d:
            root, l = d.popleft()

            if not root:
                continue

            out[l].append(root.val)

            d.append((root.left, l + 1))
            d.append((root.right, l + 1))

        for i in range(len(out)):
            if i % 2 == 1:
                ans.append(out[i][::-1])
            else:
                ans.append(out[i])

        return ans