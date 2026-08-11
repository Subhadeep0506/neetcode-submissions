class Solution:
    def rob(self, nums: List[int]) -> int:
        size = len(nums)
        if size == 1:
            return nums[size - 1]
        cache = {}
        def helper(i: int, flag: bool):
            if i >= size or (flag and i == size - 1):
                return 0
            if (i, flag) in cache:
                return cache[(i, flag)]
            cache[(i, flag)] = max(helper(i + 1, flag), helper(i + 2, flag or i == 0) + nums[i])
            return cache[(i, flag)]
        
        return max(helper(0, True), helper(1, False))