class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return [x for x in set(nums1) if x in set(nums2)]
        #return list(set(nums1).intersection(set(nums2)))
