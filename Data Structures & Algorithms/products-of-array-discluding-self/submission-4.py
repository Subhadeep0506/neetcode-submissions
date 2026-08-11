class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        size = len(nums)
        res = [1] * size
        for i in range(size):
            res[i] = prefix
            prefix = nums[i] * prefix
        postfix = 1
        for i in range(size - 1, -1, -1):
            res[i] = postfix * res[i]
            postfix = nums[i] * postfix
        return res