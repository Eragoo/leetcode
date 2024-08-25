# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        self.res = 0

        def height(root: Optional[TreeNode]) -> int:
            if not root:
                return 0
            if root and not root.left and not root.right:
                return 0

            left = height(root.left)
            right = height(root.right)

            self.res = max(self.res, left + right)

            return max(left, right) + 1


        height(root)
        return self.res
