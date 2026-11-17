class Solution:
    def maxArea(self, h: List[int]) -> int:
        l,r=0,len(h)-1
        if h[l]<=h[r]:
            vol=h[l]*(r-l)
        elif h[l]>h[r]:
            vol=h[r]*(r-l)
            
        while l<r:
            if h[l]<=h[r]:
                l+=1
            elif h[l]>h[r]:
                r-=1


            if h[l]<=h[r]:
                vol=max(vol,h[l]*(r-l))
            elif h[l]>h[r]:
                vol=max(vol,h[r]*(r-l))
            
        return vol 