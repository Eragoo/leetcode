# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot: return True
        if not root: return False

        if self.isSameTree(root, subRoot): return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


    def isSameTree(self, r: Optional[TreeNode], sr: Optional[TreeNode]) -> bool:
        if not r and not sr:
            return True
        if r and sr and r.val == sr.val:
            return self.isSameTree(r.left, sr.left) and self.isSameTree(r.right, sr.right)

        return False