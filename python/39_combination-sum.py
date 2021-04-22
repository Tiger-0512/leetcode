class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        # Define function
        def find_combinations(results, combination, candidates, target, start_index):
            if target == 0:
                results.append(combination[:])
                return

            for i in range(start_index, len(candidates)):
                if candidates[i] > target:
                    break

                combination.append(candidates[i])
                find_combinations(results, combination, candidates, target - candidates[i], i)
                combination.pop()

        results = []
        combination = []

        # Check inputs
        if not candidates or len(candidates) == 0:
            return results

        # Sort candidates
        candidates = sorted(candidates)

        find_combinations(results, combination, candidates, target, 0)

        return results