class Solution:
    # @param {integer} k
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, k, prices):
        n = len(prices)
        if n < 1:
            return 0
        if 2 * k > n:
            return self.quickSolve(n,prices)
        dp = [None for i in xrange(2*k+1)]
        dp[0] = 0
        for i in xrange(n):
            for j in xrange(1,min(2*k,i+1)+1):
                dp[j] = max(dp[j], dp[j-1]+prices[i]*[1,-1][j%2])
                
        return dp[2*k]
        
    def quickSolve(self, n, prices):
        res = 0
        for i in xrange(1,n):
            if prices[i] > prices[i-1]:
                res += prices[i] - prices[i-1]
        return res
