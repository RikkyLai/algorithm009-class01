#
# @lc app=leetcode.cn id=589 lang=python3
#
# [589] N叉树的前序遍历
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
    # 迭代法
    def preorder(self, root: 'Node') -> List[int]:
        res = []
        if not root:
            return res
        stack = [root, ]
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
            stack.extend(node.children[::-1])
        return res
        

    # 递归法    
    # def preorder(self, root: 'Node') -> List[int]:
    #     res = []
    #     self.helper(root, res)
    #     return res
    
    # def helper(self, root, res):
    #     if not root:
    #         return None
    #     res.append(root.val)
    #     for i in range(len(root.children)):
    #         self.helper(root.children[i], res)
        
# @lc code=end

