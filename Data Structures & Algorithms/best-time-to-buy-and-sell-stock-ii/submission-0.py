class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy=prices[0]
        profit=0
        sell=0
        for i in range(1,len(prices)):
            buy=min(buy,prices[i])
            sell=max(buy,prices[i])
            if sell>buy:
                revenue=sell-buy
                profit+=revenue
                buy=sell
                sell=0
        return profit
        