# Lexicographic (Binary Sorted) Subsets
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        output = []

        for i in range(2**n, 2**(n + 1)):
            bitmask = bin(i)[3:]

            tmp = []
            for i in range(n):
                if bitmask[i] == '1':
                    tmp.append(nums[i])
            output.append(tmp)

        return output


#---------------------------------------------------------------------------------------#


# Backtracking
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        def backtrack(first = 0, curr = []):
            if len(curr) == j:
                output.append(curr[:])
                return
            for i in range(first, n):
                curr.append(nums[i])
                backtrack((i + 1), curr)
                curr.pop()

        output = []
        n = len(nums)
        for j in range(n + 1):
            backtrack()

        return output


#---------------------------------------------------------------------------------------#


# Cascading
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]

        for i in nums:
            n = len(ans)
            for j in range(n):
                ans += [ans[j] + [i]]
        return ans