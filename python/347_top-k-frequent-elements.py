import heapq

'''
O(nlogn) solution with heap,
 which extract max(min) elements with O(nlogn) time complexity
 and insert elements with O(nlogn) time complexity
'''

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = dict()

        for i in nums:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1

        heap = []
        for key, value in dic.items():
            heapq.heappush(heap, (value, key))

        for i in range(len(heap) - k):
            heapq.heappop(heap)

        return [value_key[1] for value_key in heap]