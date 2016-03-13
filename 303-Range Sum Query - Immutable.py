# set up an array to store the sum from 0 to i
# then the sum from i to j = (sum from 0 to j) - (sum from 0 to i)
class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        # self.nums = nums
        value = 0
        self.alist = []
        for v in nums:
            value += v
            self.alist.append(value)
        
        

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        if i == 0:
            return self.alist[j]
        return self.alist[j] - self.alist[i-1]
        


# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.sumRange(1, 2)
