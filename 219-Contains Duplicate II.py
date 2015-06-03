class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {boolean}
    def containsNearbyDuplicate(self, nums, k):
        n = len(nums)
        if n <= 1:
            return False
        dict = {}
        for i in xrange(n):
            if nums[i] in dict and i - dict[nums[i]] <= k:
                return True
            else:
                dict[nums[i]] = i
            
            # if nums[i] not in dict:
            #     dict[nums[i]] = i
            # else:
            #     if i - dict[nums[i]] <= k:
            #         return True
            #     else:
            #         dict[nums[i]] = i
        return False
