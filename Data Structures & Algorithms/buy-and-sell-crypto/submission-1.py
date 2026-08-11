class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        profit = 0
        for sell in range(1, len(prices)):
            if prices[sell] < prices[buy]:
                buy = sell
            profit = max(profit, prices[sell] - prices[buy])
        return profit if profit > 0 else 0
        