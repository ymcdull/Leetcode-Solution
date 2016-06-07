class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # if not s:
        #     return True
        
        # l = 0
        # r = len(s) - 1
        
        # def isChar(c):
        #     if (c >= 'a' and  c <= 'z') or (c >= 'A' and c <= 'Z') or (c >= '0' and c <= '9'):
        #         return True
        #     else:
        #         return False
        
        
        # while l < r:
        #     while l < len(s) and not isChar(s[l]):
        #         l += 1
        #     while r >= 0 and not isChar(s[r]):
        #         r -= 1
        #     if l < r:
        #         if s[l].lower() != s[r].lower():
        #             return False
        #     l += 1
        #     r -= 1
        
        # return True
        
        l = filter(lambda x: x.isalnum(), s.lower())
        return l == l[::-1]
