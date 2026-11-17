class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs==[]:
            return "\0"
        s="\0".join(strs)
        return s
    def decode(self, s: str) -> List[str]:
        if s=="\0":
            return []
        strs=list(s.split("\0"))
        return strs
