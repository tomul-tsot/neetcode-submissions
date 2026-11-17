class Solution:
    def isPalindrome(self, s: str) -> bool:
        ns=[]
        for i in range(len(s)):
            if s[i].isalnum():
                ns.append(s[i].lower())
        return ns==ns[::-1]