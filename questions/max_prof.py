class Solution:
    @staticmethod
    def maxProfit(prices) -> int:
        min_price = prices[0]
        min_index = 0
        for index, price in enumerate(prices):
            if price < min_price:
                min_price = price
                min_index = index
        profit = 0
        for index in range(min_index, len(prices)):
            if prices[index] > prices[min_index] and :
                profit = prices[index] - prices[min_index]

print(Solution.maxProfit([7,6,4,3,1]))