class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {key: [] for key in range(len(nums) + 1)}
        itemCounts = collections.Counter(nums)
        
        for item, count in itemCounts.items():
            counts[count].append(item)

        res = []
        for i in range(len(counts) - 1, 0, -1):
            for item in counts[i]:
                res.append(item)
                if len(res) == k:
                    return res