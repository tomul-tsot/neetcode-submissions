class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=[]
        for i in range(len(prices)):
            for j in range(len(prices)):
                if i<j:
                    profit.append(prices[j]-prices[i])
        if len(profit)==0:
            return 0
        return max(0,max(profit))