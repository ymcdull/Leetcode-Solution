class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def containsDuplicate(self, nums):
        n = len(nums)
        if n == 0:
            return False
        dict = {}
        for i in xrange(n):
            if nums[i] in dict:
                return True
            dict[nums[i]] = 1
        return False
