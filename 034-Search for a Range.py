# Similar to binary search, after find the item, find the leftmost and rightmost item

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def searchRange(self, nums, target):
        l = 0
        r = len(nums) -1 
        while l <= r:
            mid = (l+r)/2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                list = [0, 0]
                if nums[l] == target:
                    list[0] = l
                if nums[r] == target:
                    list[1] = r
                for i in xrange(mid, r+1):
                    if nums[i] != target:
                        list[1] = i-1
                        break
                for i in xrange(mid, -1, -1):
                    if nums[i] != target:
                        list[0] = i+1
                        break
                return list
        return [-1, -1]
        
        
        
