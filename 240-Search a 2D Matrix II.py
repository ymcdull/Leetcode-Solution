# start from top-right corner, if target is larger, go downside; if target is smaller, go leftside
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        
        # num of rows
        m = len(matrix)
        # num of columns
        n = len(matrix[0])
        
        i = 0
        j = n - 1
        
        while i < m and j > -1:
            value = matrix[i][j]
            if value == target:
                return True
            elif value < target:
                i += 1
            else:
                j -= 1
                
        return False
                
        
