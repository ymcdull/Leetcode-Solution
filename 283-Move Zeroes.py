### count here means the number of non-zero values before the first zero
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        count =0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[count] = nums[count], nums[i]
                count += 1
                
