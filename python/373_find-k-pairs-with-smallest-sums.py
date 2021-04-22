class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2:
            return []

        heap = []
        ans = []

        for i in nums1[:k]:
            for j in nums2[:k]:
                heapq.heappush(heap, (i + j, [i, j]))

        for i in range(min(k, len(nums1) * len(nums2))):
            ans.append(heapq.heappop(heap)[1])

        return ans