class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        for num in nums:
            res[num] = res.get(num, 0) + 1
        return [key for key, val in sorted(res.items(), key=lambda x: x[1], reverse=True)][:k]