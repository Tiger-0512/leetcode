class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, nonzero_count = 0, 0
        n = len(nums)

        for i in range(n):
            if not nums[i] == 0:
                nums[nonzero_count] = nums[i]
                nonzero_count += 1

        for j in range(nonzero_count, n):
            nums[j] = 0