# Leetcode
# https://leetcode.com/problems/delete-leaves-with-a-given-value/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        if root.left:
            root.left = self.removeLeafNodes(root.left, target)

        if root.right:
            root.right = self.removeLeafNodes(root.right, target)

        if not root.left and not root.right:
            if root.val == target:
                return None
            return root

        return root
