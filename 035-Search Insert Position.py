class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}n
    def searchInsert(self, nums, target):
        # 二分法的变种，通过分析，最后返回l即可，同时边界条件符合当前代码，所以不需单独列出
        l = 0; r = len(nums) - 1
        while l <= r:
            m = (l+r)/2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        return l
        
