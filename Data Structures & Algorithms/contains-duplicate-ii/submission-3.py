class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        chars = {}
        for i in range(len(nums)):
            if chars.get(nums[i], None) is not None:
                if abs(i - chars[nums[i]]) <= k:
                    return True
            chars[nums[i]] = i
        return False 