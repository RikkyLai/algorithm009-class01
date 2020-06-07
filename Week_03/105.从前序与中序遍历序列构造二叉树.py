#
# @lc app=leetcode.cn id=105 lang=python
#
# [105] 从前序与中序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if inorder: 
            root = TreeNode(preorder[0])
            ind = inorder.index(root.val)
            root.left = self.buildTree(preorder[1:1+len(inorder[:ind])], inorder[:ind])
            root.right = self.buildTree(preorder[1+len(inorder[:ind]):], inorder[ind+1:])
            return root

# @lc code=end

