class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = {}
        for i, num in enumerate(numbers):
            if (target - num) in res:
                idx, alt = res[(target - num)]
                return [idx + 1, i + 1]
            else:
                res[num] = (i, target - num, )
