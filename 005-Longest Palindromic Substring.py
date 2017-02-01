## 1. Use i-th element as a centroid

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        n = len(s)
        
        if n <= 1:
            return s
            
        start = 0
        maxL = 0
        
        for i in range(n-1):
            left = right = i
            
            while left >= 0 and right <= n - 1 and s[left] == s[right]:
                left -= 1
                right += 1
            if right - left - 1 > maxL:
                maxL = right - left - 1
                start = left + 1
                
            left = i
            right = i + 1
            while left >= 0 and right <= n - 1 and s[left] == s[right]:
                left -= 1
                right += 1
            if right - left - 1 > maxL:
                maxL = right - left - 1
                start = left + 1
        
        return s[start: start + maxL]
            
            
## 2. DP
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        n = len(s)
        
        if n <= 1:
            return s
            
        start = 0
        maxL = 1
        
        dp = [[False for i in range(n)] for j in range(n)]
        
        dp[0][0] = 0
        for i in range(1, n):
            dp[i][i] = True
            dp[i][i-1] = True
        
        for k in range(2, n+1):
            for i in range(0, n-k + 1):
                if s[i] == s[i+k-1] and dp[i+1][i+k-2]:
                    dp[i][i+k-1] = True
                    if k > maxL:
                        start = i
                        maxL = k
        
        return s[start:start+maxL]
    
        
