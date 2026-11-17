class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        gand=[]
        for i in range(len(strs)):
            li=[strs[i]]
            for j in range(len(strs)):
                if len(strs[i])==len(strs[j]) and i!=j and sorted(strs[i])==sorted(strs[j]):
                    li.append(strs[j])
            if sorted(li) not in gand:
                gand.append(sorted(li))
        return gand