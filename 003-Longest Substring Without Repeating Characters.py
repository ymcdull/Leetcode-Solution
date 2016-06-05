class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        
        curStr = ""
        maxVal = 0
        for i in range(len(s)):
            if s[i] not in curStr:
                curStr += s[i]
            else:
                index = curStr.index(s[i])
                curStr = curStr[index+1:] + s[i]
            if len(curStr) > maxVal:
                maxVal = len(curStr)
        
        return maxVal
