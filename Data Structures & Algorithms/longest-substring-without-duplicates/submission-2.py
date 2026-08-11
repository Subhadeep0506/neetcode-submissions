class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique_chars = {}
        max_len = 0
        start = 0
        size = len(s)
        for end in range(size):
            if s[end] in unique_chars:
                start = max(unique_chars[s[end]] + 1, start)
            unique_chars[s[end]] = end
            max_len = max(max_len, end - start + 1)
        return max_len