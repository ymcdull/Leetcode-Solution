class Solution:
    # @param {integer[]} nums
    # @return {integer}
    
    # 类似TTS中学的Finn's method in Content Extraction
    def maxSubArray(self, nums):
        sum = 0
        max = nums[0]
        for i in xrange(len(nums)):
            sum += nums[i]
            if sum > max:
                max = sum
            if sum <= 0:
                sum = 0
        return max
