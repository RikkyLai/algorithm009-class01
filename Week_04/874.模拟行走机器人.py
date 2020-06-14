#
# @lc app=leetcode.cn id=874 lang=python3
#
# [874] 模拟行走机器人
#

# @lc code=start
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        if not commands:
            return 0
        ans = 0
        dx, dy = 0, 1
        x, y = 0, 0
        obstacle = set([(i, j) for i, j in obstacles])
        for command in commands:
            if command == -1:
                dx, dy = dy, -dx
            elif command == -2:
                dx, dy = -dy, dx
            else:
                for i in range(1, command+1):
                    if (x + dx, y + dy) in obstacle:
                        continue
                    x, y = x + dx, y + dy
                    ans = max(ans, x*x+y*y)
        return ans

        
# @lc code=end

