class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, profit = prices[0], 0
        for price in prices:
            profit = max(profit, price - buy)
            buy = min(buy, price)
        return profit