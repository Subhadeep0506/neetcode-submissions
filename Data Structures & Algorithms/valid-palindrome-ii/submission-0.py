class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        def is_palindrome(substring):
            if substring != substring[::-1]:
                return False
            return True
        
        while left < right:
            if s[left] != s[right]:
                return is_palindrome(s[left + 1: right + 1]) or is_palindrome(s[left:right])
            left += 1
            right -= 1
        
        return True