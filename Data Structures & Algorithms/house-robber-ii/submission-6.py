class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]

        def helper(_nums):
            rob1, rob2 = 0, 0
            for num in _nums:
                temp = max(rob1 + num, rob2)
                rob1 = rob2
                rob2 = temp
            return rob2
        
        return max(helper(nums[:-1]), helper(nums[1:]))