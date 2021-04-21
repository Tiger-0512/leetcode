class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Check input
        if not s:
            return 0

        # Initialization
        ans = 0
        table = {}
        j = 0

        for i, string in enumerate(s):
            if string in table:
                j = max(j, table[string] + 1)

            table[string] = i
            ans = max(ans, (i - j + 1))

        return ans