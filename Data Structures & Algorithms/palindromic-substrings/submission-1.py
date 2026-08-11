class Solution:
    def countSubstrings(self, s: str) -> int:
        size = len(s)
        count = 0
        for i in range(0, size):
            for j in range(i, size):
                sub = s[i: j+1]
                if sub == sub[::-1]:
                    count += 1
        return count