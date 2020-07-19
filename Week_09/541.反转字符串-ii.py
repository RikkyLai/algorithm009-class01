#
# @lc app=leetcode.cn id=541 lang=python3
#
# [541] 反转字符串 II
#

# @lc code=start
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        if not s:
            return ""
        res = [a for a in s]
        for i in range(0, len(res), 2*k):
            res[i:i+k] = reversed(res[i:i+k])
        return "".join(res)

        
# @lc code=end

