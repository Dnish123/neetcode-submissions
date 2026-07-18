class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        x=[]
        n = len(prices)
        for i in range(n):
            for j in range(i+1,n):
                profit = prices[j]-prices[i]
                x.append(profit)
        
        if not x:  #Handles empty case 
            return 0
        
        m = max(x)

        if m>0:
            return m
        else:
            return 0