class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = {}
        max_count = 0
        max_num = nums[0]
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
            if counts[num] > max_count:
                max_num = num
                max_count = counts[num]
        return max_num