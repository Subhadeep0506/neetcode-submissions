class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        max_len = 0
        for num in numset:
            size = 1
            if num - 1 not in numset:
                while num + size in numset:
                    size += 1
                max_len = max(max_len, size)
        return max_len