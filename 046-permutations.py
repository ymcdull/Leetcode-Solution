class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def permute(self, nums):
        n = len(nums)
        if n == 0:
            return []
        # 注意需要判断n==1的情况，否则在下边for循环的时候j会由于没有取值而使得结果出错
        if n == 1:
            return [nums]
        res = []
        for i in xrange(n):
            for j in self.permute(nums[:i]+nums[i+1:]):
                res.append([nums[i]]+j)
        return res
