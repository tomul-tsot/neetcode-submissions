class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[]
        n=len(nums)
        lp=[1]*n
        cp=1
        for i in range(n):
            lp[i]=cp
            cp*=nums[i]
        cp2=1
        rp=[1]*n
        i=0
        while i<n:
            rp[n-1-i]=cp2
            cp2*=nums[n-1-i]
            i+=1
        for i in range(n):
            res.append(lp[i]*rp[i])
        return res