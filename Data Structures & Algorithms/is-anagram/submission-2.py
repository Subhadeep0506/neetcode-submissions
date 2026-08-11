class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        _s, _t = {}, {}
        for i in range(len(s)):
            if s[i] not in _s:
                _s.update({s[i]: 1})
            else:
                _s[s[i]] += 1
            if t[i] not in _t:
                _t.update({t[i]: 1})
            else:
                _t[t[i]] += 1
        return _s == _t