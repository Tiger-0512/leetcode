class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums is None:
            return -1

        # Find pivot's index
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        index = left

        left, right = 0, len(nums) - 1

        if nums[index] <= target <= nums[-1]:
            left = index
        else:
            right = index -1

        # Binary search
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

        return -1