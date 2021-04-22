# Dynamic Programming
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0

        dp = [(0, 0)] * len(prices)  # (minimum_price, profit)
        dp[0] = (prices[0], 0)

        for i in range(1, len(dp)):
            dp[i] = (min(dp[i - 1][0], prices[i]), max(dp[i - 1][1], prices[i] - dp[i - 1][0]))

        return dp[-1][1]


#---------------------------------------------------------------------------------------#


# One Pass
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = len(prices)
        if l == 0:
            return 0

        minimum_price = prices[0]
        profit = 0

        for i in range(1, l):
            minimum_price = min(minimum_price, prices[i])
            profit = max(profit, prices[i] - minimum_price)
        return profit