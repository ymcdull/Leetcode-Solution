class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        mydict = {}
        n = len(s)
        for i in xrange(n):
            mydict.setdefault(s[i], 0)
            mydict[s[i]] += 1
        
        res = ""
        for k,v in sorted(mydict.items(), key= lambda x: x[1], reverse = True):
            res += k * v
        return res
            
