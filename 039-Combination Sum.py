class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        candidates.sort()
        res = []
        
        def dfs(currsum, lastindex, valuelist):
            if currsum == target and valuelist not in res:
                res.append(valuelist)
            
            if currsum < target:
                for i in range(lastindex, len(candidates)):
                    dfs(currsum + candidates[i], i, valuelist + [candidates[i]])
        
            return res
        
        return dfs(0, 0, [])
        
