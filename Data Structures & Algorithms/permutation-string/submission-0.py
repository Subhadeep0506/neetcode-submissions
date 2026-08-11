class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        size = len(s1)
        s1_set = dict(collections.Counter(s1))
        l, r = 0, size
        while r <= len(s2):
            sub_set = s2[l:r]
            s2_set = dict(collections.Counter(sub_set))
            if s1_set.items() == s2_set.items():
                return True
            l += 1
            r += 1
        return False