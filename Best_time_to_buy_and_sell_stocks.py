class Solution:
    def maxProfit(self, prices: List[int]) -> int: 
        sell_price = 0
        buy_price = prices[0]

        for i in range(1, len(prices)):
            profit = prices[i] - buy_price
            
            if (profit > sell_price):
                sell_price = profit

            if (prices[i] < buy_price):
                buy_price = prices[i]

        return sell_price
        
