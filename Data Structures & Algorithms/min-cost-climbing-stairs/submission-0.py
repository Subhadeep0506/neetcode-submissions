class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = {}
        n = len(cost)

        def helper(i):
            if i >= n:
                return 0
            if i in cache:
                return cache[i]
            cache[i] = min(helper(i + 1), helper(i + 2)) + cost[i]
            return cache[i]
        
        return min(helper(0), helper(1))