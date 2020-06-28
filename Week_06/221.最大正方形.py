#
# @lc app=leetcode.cn id=221 lang=python3
#
# [221] 最大正方形
#

# @lc code=start
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        maxSize = 0
        dp = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == '0' or j=='0':
                    dp[i][j] = matrix[i][j]
                elif matrix[i][j] == '1':
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
                maxSize = max(maxSize, dp[i][j])
        return maxSize**2



# @lc code=end

