## DP

class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        if not nums:
            return 0
        
        dict = {nums[0] : 1, -nums[0]: 1} if nums[0] != 0 else {0 : 2}
        
        for i in range(1, len(nums)):
            tdict = {}
            for d in dict:
                tdict[d + nums[i]] = dict.get(d, 0) + tdict.get(d + nums[i], 0)
                tdict[d - nums[i]] = dict.get(d, 0) + tdict.get(d - nums[i], 0)
            dict = tdict
        
        return dict.get(S, 0)
