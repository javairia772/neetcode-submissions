class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        minPrice = prices[0]
        maxProfit = 0
        for i in range(1, n):
            sellingPrice = prices[i]
            profit = sellingPrice - minPrice
            if sellingPrice < minPrice:
                minPrice = sellingPrice
            else:
                maxProfit = max (maxProfit, profit)

        return maxProfit

        