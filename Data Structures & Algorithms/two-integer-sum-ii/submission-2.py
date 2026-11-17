class Solution:
    def twoSum(self, n: List[int], target: int) -> List[int]:
        l,r=0,len(n)-1
        while l<r and target-n[l] not in n:
            l+=1
        while l<r and target-n[r] not in n:
            r-=1
        return [l+1,r+1]
        