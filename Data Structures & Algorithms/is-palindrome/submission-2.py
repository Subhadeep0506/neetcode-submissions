class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp = ""
        for i in range(len(s)):
            if s[i].isalnum():
                temp += s[i]
        temp = temp.lower()
        l, r = 0, len(temp) - 1
        while l < r:
            if temp[l] != temp[r]:
                return False
            l += 1
            r -= 1
        return True 