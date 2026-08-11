class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = dict()
        result = None
        for i, num in enumerate(nums):
            if res is not None and num in res:
                result = [res[num], i]
            else:
                res.update({target - num: i})
        return result