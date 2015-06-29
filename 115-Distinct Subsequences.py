class Solution:
    # @param {string} s
    # @param {string} t
    # @return {integer}
    def numDistinct(self, s, t):
        n = len(t) + 1
        m = len(s) + 1
        dp = [[0 for j in xrange(m)] for i in xrange(n)]
        for i in xrange(m):
            dp[0][i] = 1
            
        for j in xrange(1,m):
            for i in xrange(1,n):
                if s[j-1] == t[i-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i][j-1]
                else:
                    dp[i][j] = dp[i][j-1]
        return dp[n-1][m-1]
