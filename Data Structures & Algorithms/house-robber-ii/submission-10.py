class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        cache = {}
        size = len(nums)

        def helper(i, flag):
            if i >= size or (flag and i == size - 1):
                return 0
            if (i, flag) in cache:
                return cache[(i, flag)]
            cache[(i, flag)] = max(helper(i + 1, flag), helper(i + 2, flag or i == 0) + nums[i])
            return cache[(i, flag)]
        
        return max(helper(0, True), helper(1, False))