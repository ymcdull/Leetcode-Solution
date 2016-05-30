class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        #return True if num > 0 and  (4 ** 16) % num == 0 else False
        if num <=0:
            return False
        while num % 4 == 0:
            num /= 4
        return True if num == 1 else False
