#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxRight = 0
        for i in range(len(nums)):
            if i <= maxRight:
                maxRight = max(maxRight, i + nums[i])
            if maxRight >= len(nums) -1:
                return True
        return False


# @lc code=end

