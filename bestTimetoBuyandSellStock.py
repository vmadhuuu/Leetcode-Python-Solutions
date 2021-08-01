class Solution:
    def buyStock(self, prices):
        min_price = prices[0]
        max_profit = 0

        if len(prices) <1:
            return 0

        for price in prices:
            min_price = min(min_price, price)
            profit = price - min_price
            max_profit = max(max_profit, profit)
