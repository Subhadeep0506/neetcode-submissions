class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        cache = {}

        def helper(i):
            if i >= n:
                return 0
            if i in cache:
                return cache[i]

            cache[i] = max(helper(i + 2), helper(i + 3)) + nums[i]
            return cache[i]

        return max(helper(0), helper(1))