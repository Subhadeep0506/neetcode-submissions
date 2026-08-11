class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = [0] * len(nums)
        size = len(nums)
        def helper(i):
            if i >= size:
                return 0
            if cache[i] != 0:
                return cache[i]
            cache[i] = max(helper(i + 2), helper(i + 3)) + nums[i]
            return cache[i]
        
        return max(helper(0), helper(1))