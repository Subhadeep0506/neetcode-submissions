class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.max_string = s[0]
        self.max_len = 1
        
        def check_palindrome(i, j):
            while i >= 0 and j < len(s) and s[i] == s[j]:
                if len(s[i:j + 1]) > self.max_len:
                    self.max_len = j - i + 1
                    self.max_string = s[i:j + 1]
                i -= 1
                j += 1

        for i in range(len(s)):
            l, r = i, i
            check_palindrome(l, r)

            l, r = i, i + 1
            check_palindrome(l, r)
        
        return self.max_string