class Solution:
    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        res = ""
        size = len(strs)
        for s in strs:
            res = res + f"{s}<|eos|>"
        return str(size) + "<|size|>" + res

    def decode(self, s: str) -> List[str]:
        if not s or s == "":
            return []
        res = []
        size = int(s.split("<|size|>")[0])
        s = s.split("<|size|>")[-1]
        for string in s.split("<|eos|>"):
            res.append(string)
            if len(res) == size:
                break
        return res