#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def generate_(pre, left_num, right_num):
            if left_num > 0:
                generate_(pre + "(", left_num - 1, right_num)
            if right_num > left_num:
                generate_(pre+")", left_num, right_num - 1)
            if not right_num:
                res.append(pre)
            
        generate_("", n, n)
        return res
# @lc code=end

