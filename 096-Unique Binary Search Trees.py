class Solution:
    # @param {integer} n
    # @return {integer}
    
    # 对于求一共有多少个数，用dp；对于求所有可能出现的情况，用dfs
    # from: http://www.cnblogs.com/zuoyuan/p/3747824.html
    #那么这道题是使用动态规划来解决的。那么如何去求这个问题的状态转移方程呢？其实大部分动态规划的难点都是求状态转移方程。n=0时，为空树，那么dp[0]=1; n=1时，显然也是1，dp[1]=1；n=2时，dp[2]=2; 对于n>2时，dp[n]=dp[0]*dp[n-1]+dp[1]*dp[n-2]+......+dp[n-1]*dp[0]；这不就是卡特兰数的定义吗？编程很容易实现。
    # 即确定一个root，然后将left和right会出现的情况进行排列组合
    def numTrees(self, n):
        dp = [0 for i in xrange(n+1)]
        dp[0] = 1
        dp[1] = 1
        if n <= 1:
            return dp[n]
        for i in xrange(2,n+1):
            for j in range(0,i):
                dp[i] += dp[j]*dp[i-1-j]
        return dp[n]
        
