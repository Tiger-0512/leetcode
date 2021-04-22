import bisect, heapq

# O(nlogn) Solution with Binary Search; where, n = len(nums)
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = sorted(nums)

    def add(self, val: int) -> int:
        bisect.insort_left(self.nums, val)
        return self.nums[-self.k]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)


#---------------------------------------------------------------------------------------#


# O(k + n Solution with Heap; where, n = len(nums)
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = []
        sorted_n = sorted(nums, reverse=True)

        r = min(self.k, len(sorted_n))
        for i in range(r):
            heapq.heappush(self.nums, sorted_n[i])

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        if self.k == len(self.nums):
            return self.nums[0]
        else:
            heapq.heappop(self.nums)
            return self.nums[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)