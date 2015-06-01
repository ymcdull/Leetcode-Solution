class Solution:
    # @param {integer[]} nums
    # @return {integer}
    
    # Take XOR calculation for all elements
    def singleNumber(self, nums):
        res = nums[0]
        for i in range(1,len(nums)):
            res = res ^ nums[i]
        return res
