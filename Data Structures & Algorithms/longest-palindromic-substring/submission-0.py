class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.max_size = 0
        self.max_string = ""
        self.size = len(s)
        

        for i, c in enumerate(s):
            l, r = i, i
            self.check_palindrome(l, r, s)
            
            l, r = i, i + 1
            self.check_palindrome(l, r, s)
        return self.max_string
    
    def check_palindrome(self, l, r, s):
        while l >= 0 and r < self.size and s[l] == s[r]:
            if (r - l + 1) > self.max_size:
                self.max_size = r - l + 1
                self.max_string = s[l: r + 1]
            
            l -= 1
            r += 1