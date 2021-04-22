class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0

        n = len(nums)
        cumulative_s = 0
        count = 0
        dic = {0: 1}

        for i in range(n):
            cumulative_s += nums[i]
            if cumulative_s - k in dic:
                count += dic.get(cumulative_s - k)
            if cumulative_s in dic:
                dic[cumulative_s] += 1
            else:
                dic[cumulative_s] = 1

        return count