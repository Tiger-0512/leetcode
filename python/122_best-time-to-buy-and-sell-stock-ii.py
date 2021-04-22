class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0

        profit = 0
        current_price = prices[0]

        for p in prices:
            if p > current_price:
                profit += p - current_price
            current_price = p

        return profit