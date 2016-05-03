class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dict = {}
        for i in nums:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1
        alist = []
        for key,v in dict.items():
            alist.append((key,v))
        blist = sorted(alist, key=lambda tup: tup[1], reverse = True)
        return [blist[i][0] for i in range(k)]
