# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if root and not root.right and not root.left:
            return 1

        left = self.maxDepth(root.left) + 1
        right = self.maxDepth(root.right) + 1

        return max(left, right)