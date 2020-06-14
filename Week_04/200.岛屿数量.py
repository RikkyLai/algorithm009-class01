#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        count = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.bfs(grid, i, j)
                    count += 1
        return count

    def bfs(self, grid, i, j):
        if i < 0 or j < 0 or j > len(grid[0])-1 or i > len(grid) - 1 or grid[i][j]!= '1':
            return
        grid[i][j] = '#'
        self.bfs(grid, i+1, j)
        self.bfs(grid, i-1, j)
        self.bfs(grid, i, j-1)
        self.bfs(grid, i, j+1)
# @lc code=end

