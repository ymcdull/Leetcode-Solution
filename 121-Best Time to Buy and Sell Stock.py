class Solution:
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, prices):
        if len(prices) <= 1:
            return 0
        minV = prices[0]
        profit = 0
        for i in range(1,len(prices)):
            profit = max(prices[i]-minV, profit)
            minV = min(minV, prices[i])
        return profit
