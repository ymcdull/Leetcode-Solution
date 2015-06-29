class Solution:
    # @param {integer[]} nums
    # @return {string[]}
    def summaryRanges(self, nums):
        if not nums:
            return []
        res = []
        tmp = 0
        for i in xrange(1,len(nums)):
            if nums[i] != nums[i-1] + 1:
                if tmp != i-1:
                    res.append(str(nums[tmp])+'->'+str(nums[i-1]))
                else:
                    res.append(str(nums[tmp]))    
                tmp = i
        if nums[tmp] != nums[-1]:
            res.append(str(nums[tmp])+'->'+str(nums[-1]))
        else:
            res.append(str(nums[tmp]))
        return res
            
                
        
