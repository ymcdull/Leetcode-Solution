class Solution:
    # @param {integer[][]} matrix
    # @param {integer} target
    # @return {boolean}
    def searchMatrix(self, matrix, target):
        m = len(matrix)
        n = len(matrix[0])
        top = 0
        right = n - 1
        # 每次判断右上角的元素
        while top <= m-1 and right >= 0:
            if target == matrix[top][right]:
                return True
            elif target < matrix[top][right]:
                right -= 1
            else:
                top += 1
        return False
