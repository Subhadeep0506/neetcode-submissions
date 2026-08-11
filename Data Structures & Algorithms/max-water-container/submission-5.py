class Solution:
    def maxArea(self, heights: List[int]) -> int:
        size = len(heights)
        l, r = 0, size - 1
        max_vol = 0
        while l < r:
            height = min(heights[l], heights[r])
            max_vol = max(max_vol, height * (r - l))
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return max_vol