class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        
        m = len(haystack)
        n = len(needle)
        
        for i in range(m-n+1):
            flag = True
            for j in range(n):
                if needle[j] != haystack[i+j]:
                    flag = False
                    break
            if flag == True:
                return i
            
            
        return -1
