#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return []
        res = []
        self.dfs(nums, [], res)
        return res

    def dfs(self, nums, pre, res):
        if len(nums) == 0:
            res.append(pre[:])
            return
        for i in range(len(nums)):
            pre.append(nums[i])
            res_nums = nums[:i] + nums[i+1:]
            self.dfs(res_nums, pre, res)
            pre.pop()

# @lc code=end

