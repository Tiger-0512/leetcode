class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] < nums[-1] or len(nums) == 1:
            return nums[0]

        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            if nums[mid - 1] > nums[mid]:
                return nums[mid]

            if nums[left] > nums[mid]:
                right = mid - 1
            else:
                left = mid + 1