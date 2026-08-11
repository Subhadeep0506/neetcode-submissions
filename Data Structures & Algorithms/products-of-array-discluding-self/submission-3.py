class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        zero_count = 0
        for num in nums:
            if num != 0:
                prod *= num
            else:
                zero_count += 1
        if zero_count > 1: return [0] * len(nums)
        res = [0] * len(nums)

        for idx, num in enumerate(nums):
            if num:
                res[idx] = prod // num if zero_count < 1 else 0
            else:
                res[idx] = prod 
        return res