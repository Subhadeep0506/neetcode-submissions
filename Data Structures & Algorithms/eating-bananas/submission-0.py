class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start, end = 1, max(piles)
        k_threshold = max(piles)
        total = sum(piles)
        while start <= end:
            mid = (start + end) // 2
            time = 0
            for pile in piles:
                time += math.ceil(float(pile) / mid)
            if time <= h:
                k_threshold = mid
                end = mid - 1
            else:
                start = mid + 1 
        return k_threshold