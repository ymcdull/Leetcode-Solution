class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        def get_dict(in_list):
            dict = {}
            for i in in_list:
                if i in dict:
                    dict[i] += 1
                else:
                    dict[i] = 1
            return dict
            
            
        dict1 = get_dict(nums1)
        dict2 = get_dict(nums2)
        
        res = []
        for k,v in dict1.items():
            if k in dict2:
                value = dict2[k]
                res.extend([k] * min(v, value))
                
        return res
            
