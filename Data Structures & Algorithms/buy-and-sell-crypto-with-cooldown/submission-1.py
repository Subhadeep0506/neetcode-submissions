class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cache = {}
        n = len(prices)
        if n < 2:
            return 0
        def dfs(i, buying):
            if i >= n:
                return 0
            if (i, buying) in cache:
                return cache[(i, buying)]
            cooldown = dfs(i + 1, buying)
            if buying:
                buy = dfs(i + 1, not buying) - prices[i]
                cache[(i, buying)] = max(cooldown, buy)
            else:
                sell = dfs(i + 2, not buying) + prices[i]
                cache[(i, buying)] = max(cooldown, sell)
            return cache[(i, buying)]
        return dfs(0, True)