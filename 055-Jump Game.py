class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        m = 0
        for i in range(len(nums)):
            if i <= m:
                m = max(nums[i] + i, m)
                if m >= len(nums) - 1:
                    return True
        return False
