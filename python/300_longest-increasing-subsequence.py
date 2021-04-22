import bisect

# O(n^2) Solution with Dynamic Programming
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        dp = [0] * n
        dp[0] = 1
        ans = 1

        for i in range(1, n):
            val = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    val = max(val, dp[j])
            dp[i] = val + 1
            ans = max(ans, dp[i])

        return ans


#---------------------------------------------------------------------------------------#


# O(nlogn) Solution with Dynamic Programming and My Binary Search
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)

        dp = []
        dp.append(nums[0])

        for i in range(1, n):
            if dp[-1] < nums[i]:
                dp.append(nums[i])
            else:
                index = self.binary_search(dp, nums[i])
                dp[index] = nums[i]

        return len(dp)


    def binary_search(self, arr, num):
        left, right = 0, len(arr)

        while left < right:
            mid = (left + right) // 2
            if arr[mid] == num:
                return mid
            elif arr[mid] > num:
                right = mid
            else:
                left = mid + 1

        return left


#---------------------------------------------------------------------------------------#


# O(nlogn) Solution with Dynamic Programming and bisect
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)

        dp = []
        dp.append(nums[0])

        for i in range(1, n):
            if dp[-1] < nums[i]:
                dp.append(nums[i])
            else:
                index = bisect.bisect_left(dp, nums[i])
                dp[index] = nums[i]

        return len(dp)


#---------------------------------------------------------------------------------------#


# O(nlogn) Solution with Dynamic Programming and bisect
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)

        dp = [0] * (n)
        dp[0] = nums[0]
        length = 1

        for i in range(1, n):
            if dp[length - 1] < nums[i]:
                dp[length] = nums[i]
                length += 1
            else:
                index = bisect.bisect_left(dp, nums[i], 0, length)
                dp[index] = nums[i]

        return length