#
# @lc app=leetcode.cn id=32 lang=python3
#
# [32] 最长有效括号
#

# @lc code=start
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        m = len(s)
        if not m:
            return 0
        dp = [0]*m
        for i in range(1, m):
            if s[i] == ')' and i - dp[i-1]-1 >=0 and s[i-dp[i-1]-1] == '(':
                dp[i] = dp[i-1] + 2 + dp[i-dp[i-1]-2]
        return max(dp)

# @lc code=end

