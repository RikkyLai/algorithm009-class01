#
# @lc app=leetcode.cn id=429 lang=python3
#
# [429] N叉树的层序遍历
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        res = []
        if not root:
            return res
        level = [root]
        while level:
            res.append(i.val for i in level)
            l = []
            for node in level:
                for child in node.children:
                    l.append(child)
            level = l
        return res
        
# @lc code=end

