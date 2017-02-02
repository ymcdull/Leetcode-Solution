class Solution:
    # @param {integer[]} nums1
    # @param {integer[]} nums2
    # @return {float}
    
    def findMedianSortedArrays(self, nums1, nums2):
        m = len(nums1)
        n = len(nums2)
        
        if (m + n) % 2 == 1:
            return self.getKth(nums1, nums2, (m+n)/2+1) * 1.0
        else:
            return (self.getKth(nums1, nums2, (m+n)/2) + self.getKth(nums1, nums2, (m+n)/2+1)) * 0.5
    
    def getKth(self, A, B, k):
        m = len(A)
        n = len(B)
        
        if m > n:
            return self.getKth(B, A, k)
            
        if m == 0:
            return B[k-1]
            
        if k == 1:
            return min(A[0], B[0])
            
        pa = min(k/2, m)
        pb = k - pa
        
        if A[pa - 1] < B[pb - 1]:
            return self.getKth(A[pa:], B, k - pa)
        else:
            return self.getKth(A, B[pb:], k - pb)
        
   
