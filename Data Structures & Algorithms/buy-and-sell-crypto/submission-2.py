class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bp=prices[0]
        diff=0
        for i in range(len(prices)):
            bp=min(bp,prices[i])
            diff=max(diff,prices[i]-bp)
        return diff
        

