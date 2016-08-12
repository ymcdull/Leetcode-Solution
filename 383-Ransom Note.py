class Solution(object):
    
    def to_dict(self, s):
        dict = {}
        for w in s:
            if w not in dict:
                dict[w] = 1
            else:
                dict[w] += 1
        return dict
    
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        r = self.to_dict(ransomNote)
        m = self.to_dict(magazine)
        
        for k,v in r.items():
            if k not in m or r[k] > m[k]:
                return False

        return True
