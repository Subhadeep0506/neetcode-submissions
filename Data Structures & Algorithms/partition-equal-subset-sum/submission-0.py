class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        cache = {}
        total = sum(nums)
        n = len(nums)
        def dfs(i, curr_sum):
            if i >= n or curr_sum > total / 2:
                return False
            if curr_sum == total / 2:
                return True
            if (i, curr_sum) in cache:
                return cache[(i, curr_sum)]
            cache[(i, curr_sum)] = dfs(i + 1, curr_sum + nums[i]) or dfs(i + 2, curr_sum + nums[i])
            return cache[(i, curr_sum)]
        
        for i in range(n):
            if dfs(i, 0):
                return True
            else:
                continue
        return False