class Solution:
    def findMin(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1
        res = float("inf")
        while start <= end:
            if nums[start] < nums[end]:
                res = min(res, nums[start])
                break
            mid = (start + end) // 2
            res = min(res, nums[mid])
            if nums[mid] < nums[end]:
                end = mid - 1
            else:
                start = mid + 1
        return res