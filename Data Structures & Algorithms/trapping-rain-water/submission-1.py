class Solution:
    def trap(self, h: List[int]) -> int:
        if not h:
            return 0
        water=0
        l,r=0,len(h)-1
        for i in range(1,len(h)-1):
            l=max(h[0:i])
            r=max(h[i+1:])
            water+=max(0,min(l,r)-h[i])
        return water
