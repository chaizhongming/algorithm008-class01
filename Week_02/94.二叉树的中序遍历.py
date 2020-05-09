#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        traversal_path=[]
        def inorder(root):
            if root:
                inorder(root.left)
                traversal_path.append(root.val)
                # print(self.traversal_path)
                inorder(root.right)
            # self.inorderTraversal(root)
        inorder(root)
        return traversal_path
# @lc code=end

