class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board
            
        else:
            self.dfs(board, click)
            return board
            
    def dfs(self, board, click):
        m,n = click[0], click[1]
        nrow = len(board)
        ncol = len(board[0])
        
        u = max(0, m-1)
        d = min(nrow-1, m+1)
        l = max(0, n-1)
        r = min(ncol-1, n+1)
        
        count = 0
        for i in range(u, d+1):
            for j in range(l, r+1):
                if i == m and j == n:
                    continue
                if board[i][j] == 'M':
                    count += 1
        if count == 0:
            board[m][n] = 'B'
            for i in range(u, d+1):
                for j in range(l, r+1):
                    if i == m and j == n:
                        continue
                    if not (board[i][j] == 'E'):
                        continue
                    # if board[i][j] == 'B':
                    self.dfs(board, [i,j])
        else:
            board[m][n] = str(count)
