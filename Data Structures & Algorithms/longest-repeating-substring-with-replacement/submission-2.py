class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        chars = {}
        l = 0
        max_len = 0
        max_count = 0
        for r in range(len(s)):
            chars[s[r]] = chars.get(s[r], 0) + 1
            max_count = max(max_count, chars[s[r]])

            while (r - l + 1) - max_count > k:
                chars[s[l]] -= 1
                l += 1

            max_len = max(r - l + 1, max_len)
        return max_len