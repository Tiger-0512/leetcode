# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None

        size = len(nums)

        if size == 1:
            return TreeNode(val=nums[0])
        else:
            root_idx = size // 2

            root = TreeNode(val=nums[root_idx])
            root.left = self.sortedArrayToBST(nums[:root_idx])
            root.right = self.sortedArrayToBST(nums[(root_idx + 1):])

            return root