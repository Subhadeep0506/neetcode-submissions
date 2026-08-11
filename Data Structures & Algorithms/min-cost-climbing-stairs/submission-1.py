class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        size = len(cost)
        def helper(i):
            if i >= size:
                return 0
            return min(helper(i + 1), helper(i + 2)) + cost[i]
        return min(helper(0), helper(1))