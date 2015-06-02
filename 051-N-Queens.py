class Solution:
    # @return a list of lists of string
    def solveNQueens(self, n):
        def check(k,j): # 在第k行是否可以放在第k列
            for i in xrange(k):
                if board[i] == j or abs(k-i) == abs(j-board[i]):
                    return False
            return True
        
        def dfs(valuelist, val):
            if val == n:
                res.append(valuelist)
                return
            for i in xrange(n):
                if check(val, i):
                    board[val] = i
                    s = '.'*n
                    dfs(valuelist+[s[:i]+'Q'+s[i+1:]], val+1)
        
        board = [-1 for i in xrange(n)]
        res = []
        dfs([],0)
        return res
