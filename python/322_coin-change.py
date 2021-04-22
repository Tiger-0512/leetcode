'''
O(k*n) Solution with Dynamic Programming
 by referring to https://www.youtube.com/watch?v=ZI17bgz07EE
k: amount
n: the number of coins

DP table is below

coins = [1, 2, 5], amount = 11
i         0 1 2 3 4 5 6 7 8 9 10 11
[]        0 ∞ ∞ ∞ ∞ ∞ ∞ ∞ ∞ ∞  ∞  ∞
[1]       0 1 2 3 4 5 6 7 8 9 10 11
[1, 2]    0 1 1 2 2 3 3 4 4 5  5  6
[1, 2, 5] 0 1 1 2 2 1 2 2 3 3  2  3
'''

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        n = len(coins)

        dp = [[0 for i in range(amount + 1)] for j in range(n + 1)]
        for j in range(1, amount + 1):
            dp[0][j] = float('inf')
        for i in range(n + 1):
            dp[i][0] = 0

        for i in range(1, n + 1):
            for j in range(1, amount + 1):
                if coins[i - 1] > j:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = min(dp[i - 1][j], 1 + dp[i][j - coins[i - 1]])

        return dp[-1][-1] if not dp[-1][-1] == float('inf') else -1


#---------------------------------------------------------------------------------------#

'''
O(k*n) Solution with Dynamic Programming
k: amount
n: the number of coins
'''
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        n = len(coins)

        dp = [[0 for i in range(amount + 1)] for j in range(n + 1)]

        for i in range(n + 1):
            for j in range(amount + 1):
                if i == 0:
                    dp[i][j] = float('inf')
                elif j == 0:
                    dp[i][j] = 0
                elif coins[i - 1] > j:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = min(dp[i - 1][j], 1 + dp[i][j - coins[i - 1]])

        return dp[-1][-1] if not dp[-1][-1] == float('inf') else -1