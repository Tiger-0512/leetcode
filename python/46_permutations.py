class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Variables
        results = []
        permutation = []

        # Check Input
        if not nums:
            return results

        # Execute function
        self.find_permutations(results, permutation, nums)

        return results


    # Define function
    def find_permutations(self, results, permutation, nums):
        if not nums:
            results.append(permutation[:])
            return

        for i in range(len(nums)):
            permutation.append(nums[i])
            self.find_permutations(results, permutation, nums[:i] + nums[(i + 1):])
            permutation.pop()