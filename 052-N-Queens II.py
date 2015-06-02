class Solution:
    # @param {integer} n
    # @return {integer}
    def totalNQueens(self, n):
        def isValid(k,j): # check if can be put at row k and column j
            for i in range(0,k):
                if board[i] == j or abs(k-i) == abs(board[i]-j):
                    return False
            return True
            
        def dfs(k, valuelist):
            if k == n:
                res.append(valuelist)
                return
            for j in xrange(n):
                if isValid(k,j):
                    board[k] = j
                    s = '.'*n
                    dfs(k+1, valuelist+[s[:j]+'Q'+s[j+1:]])
        res = []
        board = [-1 for i in xrange(n)]
        dfs(0, [])
        return len(res)
                
