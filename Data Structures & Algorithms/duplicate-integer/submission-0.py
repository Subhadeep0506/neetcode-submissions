class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_hash = dict()
        for num in nums:
            if num in nums_hash:
                return True
            else:
                nums_hash.update({num: 1})
        return False