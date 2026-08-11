class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for idx, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                _idx, _temp = stack.pop()
                res[_idx] = idx - _idx
            stack.append((idx, temp))
        return res