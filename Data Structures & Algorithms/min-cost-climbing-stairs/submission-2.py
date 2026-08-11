class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        cache = [0] * n
        
        def helper(i):
            if i >= n:
                return 0
            if cache[i]:
                return cache[i]
            cache[i] = min(helper(i + 1), helper(i + 2)) + cost[i]
            return cache[i]
        
        return min(helper(0), helper(1))