class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def backtrack(s, left, right):
            if len(s) == 2 * n:
                ans.append(s)
                return
            if left < n:
                backtrack(s + '(', left + 1, right)
            if right < n and left > right:
                backtrack(s + ')', left, right + 1)

        backtrack('', 0, 0)

        return ans