class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self, nums, target):
        dict = {}  # use dict to store values we have seen
        for i in xrange(len(nums)):
            if target - nums[i] in dict:
                return [dict[target-nums[i]]+1, i+1]
            dict[nums[i]] = i
