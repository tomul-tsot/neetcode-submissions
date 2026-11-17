class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        s=sorted(nums)
        res=set()
        for k in range(len(s)):
            if k > 0 and nums[k] == nums[k-1]:
                continue
            l,r=k+1,len(s)-1
            while l<r:
                if s[l]+s[r]+s[k]>0:
                    r-=1
                elif s[l]+s[r]+s[k]<0:
                    l+=1
                else:
                    res.add((s[k],s[l],s[r]))
                    l+=1
                    r-=1
                    while s[l]==s[l-1] and l<r:
                        l+=1
        res == sorted(res)
        return [list(t) for t in res]