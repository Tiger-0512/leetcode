# O(n) solution with Pointer
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = float('inf')
        left, cur_sum = 0, 0

        for i in range(len(nums)):
            cur_sum += nums[i]

            while cur_sum >= target:
                min_len = min(min_len, i - left + 1)

                cur_sum -= nums[left]
                left += 1

        return min_len if min_len != float('inf') else 0


#---------------------------------------------------------------------------------------#


# O(nlogn) Solution with Binary Search
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0

        ans = float('inf')
        sums = [0] * (n + 1)
        sums[0] = 0

        # cumulative sum
        for i in range(1, n + 1):
            sums[i] = sums[i - 1] + nums[i - 1]

        i, j = 0, 1
        while j < (n + 1):
            while sums[j] - sums[i] >= target:
                ans = min(ans, j - i)
                i += 1
            j += 1

        return ans if ans != float('inf') else 0