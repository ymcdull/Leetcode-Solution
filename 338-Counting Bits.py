##DP
class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        
        ## dp[index - offset]
        
        dp = [0]
        offset = 1
        for index in range(1, num + 1):
            if index == offset * 2:
                offset *= 2
            dp.append(dp[index - offset] + 1)
            
        return dp
            
        
