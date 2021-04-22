class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_current = max_global = nums[0]

        if len(nums) == 1:
            return max_global

        for i in range(1, len(nums)):
            max_current = max(max_current + nums[i], nums[i])
            if max_global < max_current:
                max_global = max_current

        return max_global