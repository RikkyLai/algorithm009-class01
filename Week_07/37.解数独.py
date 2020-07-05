#
# @lc app=leetcode.cn id=37 lang=python3
#
# [37] 解数独
#

# @lc code=start
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.board = board
        self.solve()

    def findUnasigned(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == '.':
                    return i, j
        return -1, -1

    def solve(self):
        row, col = self.findUnasigned()
        if row == -1 and col == -1:
            return True
        for num in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            if self.safe(row, col, num):
                self.board[row][col] = num
                if self.solve():
                    return True
                self.board[row][col] = '.'
        return False

    def safe(self, row, col, num):
        for r in range(9):
            if self.board[r][col]==num:
                return False
        for c in range(9):
            if self.board[row][c]==num:
                return False
        boxrow = row - row%3
        boxcol = col - col%3
        for i in range(boxrow, boxrow+3):
            for j in range(boxcol, boxcol+3):
                if self.board[i][j]==num:
                    return False

        return True
# @lc code=end

