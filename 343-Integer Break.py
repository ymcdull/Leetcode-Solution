# O(1) method, not a good way as I suppose
class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        rest = n % 3
        a = n / 3
        
        if n == 2:
            return 1
        if n == 3:
            return 2
        
        if rest == 0:
            ret = 3 ** a
        elif rest == 2:
            ret = (3 ** a) * 2
        else:
            ret = (3 ** (a-1)) * 4
                
        return ret
        
        # O(n) DP method:
        m = [0 for i in range(n+1)]
        m[1] = 1
        for i in range(2, n+1):
            alist = [j * max(i-j, m[i-j])  for j in range(1,i)]
            m[i] = max(alist)
        return m[n]
        
        
