class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        tmp = x
        val = 0
        while x > 0:
            rest = x % 10
            x /= 10
            val = val * 10 + rest
            
        if val == tmp:
            return True
        else:
            return False
