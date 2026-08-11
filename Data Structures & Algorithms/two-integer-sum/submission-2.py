class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pairs = {}
        for idx, num in enumerate(nums):
            if target - num in pairs:
                return [pairs[target - num], idx]
            pairs[num] = idx