class Solution:
    # @param {string[]} strs
    # @return {string}
    def longestCommonPrefix(self, strs):
        if not strs:
            return ''
        min = len(strs[0])
        for i in xrange(len(strs)):
            if len(strs[i]) < min:
                min = len(strs[i])
        for i in range(min,-1,-1):
            flag = 0
            for j in xrange(len(strs)):
                if strs[0][:i] != strs[j][:i]:
                    flag = 1
                    break
            if flag == 0:
                return strs[0][:i]
        return ''
            
            
            
        
