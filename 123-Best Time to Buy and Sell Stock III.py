class Solution:
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, prices):
        n = len(prices)
        if n == 0:
            return 0
        f1 = [0 for i in xrange(n)]
        f2 = [0 for i in xrange(n)]
        
        minV = prices[0]
        for i in range(1,n):
            # if prices[i] - minV > f1[i-1]:
            #     f1[i] = prices[i] - minV
            # else:
            #     f1[i] = f1[i-1]
            
            # 可以用下边一行替代上边四行
            f1[i] = max(prices[i]-minV, f1[i-1])
            minV = min(prices[i], minV)
        
        maxV = prices[n-1]
        for i in range(n-2,-1,-1):
            f2[i] = max(maxV-prices[i], f2[i+1])
            maxV = max(maxV, prices[i])
        
        res = 0
        for i in xrange(n):
            res = max(f1[i]+f2[i], res)
        return res
