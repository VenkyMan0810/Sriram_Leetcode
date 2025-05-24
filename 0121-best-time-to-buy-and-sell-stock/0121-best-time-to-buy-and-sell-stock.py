class Solution(object):
    def maxProfit(self, prices):
        min_price = float('inf')
        max_profit = 0

        for i in range(len(prices)):
            min_price = min(min_price, prices[i])
            curr = prices[i] - min_price 
            max_profit = max(max_profit, curr)
        
        return max_profit

        