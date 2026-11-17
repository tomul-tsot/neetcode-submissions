class Solution:
    def maxArea(self, h: List[int]) -> int:
        v=set()
        l,r=0,len(h)-1
        while l<r:
            if h[l]<=h[r]:
                v.add(h[l]*(r-l))
                l+=1
            elif h[l]>h[r]:
                v.add(h[r]*(r-l))
                r-=1
        return max(v)  
