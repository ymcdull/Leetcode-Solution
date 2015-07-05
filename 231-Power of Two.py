class Solution:
    # @param {integer} n
    # @return {boolean}
    def isPowerOfTwo(self, n):
        # Recursion method
        if n <= 0:
            return False
        if n == 1:
            return True
        if n % 2 != 0:
            return False
        return self.isPowerOfTwo(n/2)
        
        # Iteration method
        # if n <= 0:
        #     return False
        # while n >= 1:
        #     if n == 1:
        #         return True
        #     if n % 2 != 0:
        #         return False
        #     n = n / 2
