class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        flag = False

        i = len(nums) - 2
        while i >= 0 and nums[i + 1] <= nums[i]:
            i -= 1
        if i == -1:
            i = 0
            flag = True

        if not flag:
            j = len(nums) - 1
            while j >= 0 and nums[j] <= nums[i]:
                j -= 1

            nums[i], nums[j] = nums[j], nums[i]
            i += 1

        j = len(nums) - 1
        while i <= j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1