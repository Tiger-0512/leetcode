from math import factorial

class Solution:
    def nCr(self, n, r):
        return factorial(n) / factorial(r) / factorial(n - r)

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0] * n for i in range(m)]

        if obstacleGrid[0][0] == 1:
            return 0
        else:
            dp[0][0] = 1

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    if not i == 0:
                        dp[i][j] += dp[i - 1][j]
                    if not j == 0:
                        dp[i][j] += dp[i][j - 1]

        return dp[-1][-1]