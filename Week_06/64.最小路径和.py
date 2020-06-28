#
# @lc app=leetcode.cn id=64 lang=python3
#
# [64] 最小路径和
#

# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        dp = [0]*n
        for i in range(m):
            for j in range(n):
                if i == 0 and j!=0:
                    dp[j] = grid[i][j] + dp[j-1]
                elif j==0:
                    dp[j] = grid[i][j] + dp[j]
                else:
                    dp[j] = grid[i][j] + min(dp[j], dp[j-1])
        return dp[-1]
# @lc code=end

