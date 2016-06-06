class Solution(object):
    def combinationSum2(self, candidates, target):
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
                return 
            
            if currsum < target:
                for i in range(lastindex, len(candidates)):
                    dfs(currsum + candidates[i], i + 1, valuelist + [candidates[i]])
            
        dfs(0, 0, [])
        
        return res
