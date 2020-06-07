#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if n*k == 0 or k > n:
            return []
        res = []
        self.dfs(1, n, k, [], res)
        return res
    
    def dfs(self, start, n, k, pre, res):
        if len(pre) == k:
            res.append(pre[:])
            return

        for i in range(start, n+1):
            pre.append(i)
            self.dfs(i+1, n, k, pre, res)
            pre.pop()

# @lc code=end

