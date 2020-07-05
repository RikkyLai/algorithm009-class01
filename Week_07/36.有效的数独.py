#
# @lc app=leetcode.cn id=36 lang=python3
#
# [36] 有效的数独
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        self.board = board
        return self.valid()

    def valid(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] != '.':
                    if not self.safe(i, j):
                        return False
        return True

    def safe(self, row, col):
        for c in range(9):
            if c!=col and self.board[row][c] == self.board[row][col]:
                return False
        for r in range(9):
            if r != row and self.board[r][col] == self.board[row][col]:
                return False
        boxrow = row - row%3
        boxcol = col - col%3
        for i in range(boxrow, boxrow+3):
            for j in range(boxcol, boxcol+3):
                if i!=row and j != col and self.board[i][j] == self.board[row][col]:
                    return False
        return True
            
# @lc code=end

