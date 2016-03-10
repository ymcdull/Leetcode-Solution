class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        if not words:
            return 0
            
        process = [0 for i in range(len(words))]
        
        for i in range(len(words)):
            for j in range(len(words[i])):
                process[i] |= 1 << ord(words[i][j]) - 97
                
        maxValue = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if process[i] & process[j] == 0 and len(words[i]) * len(words[j]) > maxValue:
                    maxValue = len(words[i]) * len(words[j])
                    
        return maxValue
