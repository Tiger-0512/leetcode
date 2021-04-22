import math

class Solution:
    def nCr(self, n, r):
        return math.factorial(n) / math.factorial(r) / math.factorial(n - r)

    def uniquePaths(self, m: int, n: int) -> int:
        return int(self.nCr((m + n - 2), (m - 1)))