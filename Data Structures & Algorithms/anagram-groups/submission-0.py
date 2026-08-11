class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups: dict[List[str]] = {}
        for word in strs:
            ref = "".join(sorted(word))
            if ref not in groups:
                groups.update({ref: [word]})
            else:
                groups[ref].append(word)
        return list(groups.values())