class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        # return s[::-1]
        return ''.join(s[i] for i in range(len(s)-1, -1, -1))
