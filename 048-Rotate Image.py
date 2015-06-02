class Solution:
    # @param {integer[][]} matrix
    # @return {void} Do not return anything, modify matrix in-place instead.
    def rotate(self, matrix):
        n = len(matrix)
        # 先转置，再column中心对称调换
        for i in xrange(n):
            for j in range(i+1,n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]  
        for i in xrange(n):
            for j in xrange(n/2):
                matrix[i][j], matrix[i][n-1-j] = matrix[i][n-1-j],matrix[i][j]
                
