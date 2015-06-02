class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {integer[][]}
    def combine(self, n, k):
        def dfs(lastindex, valuelist):
            if len(valuelist) == k:
                res.append(valuelist)
                return
            for i in range(lastindex,n):
                dfs(i+1, valuelist+[alist[i]])
        
        alist = [i for i in range(1,n+1)]    
        res = []
        dfs(0,[])
        return res    
            
        
