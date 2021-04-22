# Dynamic Programming Solution with Based on House Robber 1
class Solution:
    def rob(self, nums: List[int]) -> int:

        def find_max(nums):
            prev_max = 0
            cur_max = 0

            for n in nums:
                tmp = cur_max
                cur_max = max(cur_max, prev_max + n)
                prev_max = tmp

            return cur_max

        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        return max(find_max(nums[:-1]), find_max(nums[1:]))