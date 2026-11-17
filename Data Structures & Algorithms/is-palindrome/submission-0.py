class Solution:
    def isPalindrome(self, s: str) -> bool:
        ns=""
        for i in range(len(s)):
            if s[i].isalnum()==True:
                ns+=s[i].lower()
        rns=ns[::-1]
        rns="".join(rns)
        print(ns)
        print(rns)
        if ns==rns:
            return True
        return False