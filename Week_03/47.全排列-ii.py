#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        nums.sort()
        res = []
        self.dfs(nums, [], res)
        return res

    def dfs(self, nums, pre, res):
        if len(nums) == 0:
            res.append(pre[:])
            return 
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            pre.append(nums[i])
            res_nums = nums[:i] + nums[i+1:]
            self.dfs(res_nums, pre, res)
            pre.pop()
# @lc code=end

