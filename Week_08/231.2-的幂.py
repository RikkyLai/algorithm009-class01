#
# @lc app=leetcode.cn id=231 lang=python3
#
# [231] 2的幂
#

# @lc code=start
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if not n:
            return False
        n = n&(n-1)
        if not n:
            return True
        return False
# @lc code=end

