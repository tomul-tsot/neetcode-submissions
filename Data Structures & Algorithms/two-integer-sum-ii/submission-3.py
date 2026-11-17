class Solution:
    def twoSum(self, n: List[int], target: int) -> List[int]:
        l,r=0,len(n)-1
        while l<r:
            if n[l]+n[r]<target:
                l+=1
            elif n[l]+n[r]>target:
                r-=1
            else:
                return [l+1,r+1]