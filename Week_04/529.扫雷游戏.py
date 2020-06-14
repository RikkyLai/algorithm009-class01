#
# @lc app=leetcode.cn id=529 lang=python3
#
# [529] 扫雷游戏
#

# @lc code=start
d = ((1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1))
class Solution:
    
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        a, b = click
        if board[a][b] == 'M':
            board[a][b] = 'X'
        elif board[a][b] == 'E':
            m, n = len(board), len(board[0])
            def f(i, j):
                c = 0
                for di, dj in d:
                    x, y = i + di, j + dj
                    if 0 <= x < m and 0 <= y < n:
                        c += board[x][y] == 'M'
                if c:
                    board[i][j] = str(c)
                else:
                    board[i][j] = 'B'
                    for di, dj in d:
                        x, y = i + di, j + dj
                        0 <= x < m and 0 <= y < n and board[x][y] == 'E' and f(x, y)
            f(a, b)
        return board
            
        
        
# @lc code=end

