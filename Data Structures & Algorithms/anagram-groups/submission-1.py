class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for string in strs:
            char_counts = [0] * 26
            for char in string:
                char_counts[ord(char) - ord('a')] +=  1
            res[tuple(char_counts)].append(string)
        return list(res.values())