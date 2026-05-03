class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L=0
        n=len(prices)
        R=1
        profit=0
        res=0

        while R<n:
            if prices[L]>prices[R]:
                L=R
            else:
                profit=prices[R]-prices[L]
                res=max(profit,res)
            R+=1
            
        return res