class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        S={}
        T={}
        for i in range(len(s)):
            if s[i] in S:
                S[s[i]]+=1
            elif s[i] not in S:
                S[s[i]]=1
        
        for i in range(len(t)):
            if t[i] in T:
                T[t[i]]+=1
            elif t[i] not in T:
                T[t[i]]=1

        if S==T:
            return True
        return False
            