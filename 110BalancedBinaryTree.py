# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True
        if not root or (not root.left and not root.right):
            return True
        def height(curr: Optional[TreeNode]) -> int:
            if not curr:
                return 0

            left = height(curr.left)
            right = height(curr.right)

            if abs(left - right) <= 1:
                self.balanced = False

            return max(left, right) + 1


        height(root)
        return self.balanced