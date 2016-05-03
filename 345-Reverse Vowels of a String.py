class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = set(['a','e','i','o','u','A', 'E','I','O','U'])
        
        
        n = len(s)
        s = list(s)
        l = 0 
        r = n - 1

        
        while l < r:
            
            while l < n and s[l] not in vowels:
                l += 1
            while r > 0 and s[r] not in vowels:
                r -= 1
            
            if l >= r:
                break
            else:
                s[l], s[r] = s[r], s[l]
                l,r = l+1, r-1
            
            
        return ''.join(s)
        
