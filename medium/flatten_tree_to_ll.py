# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        right = root.right
        root.right = root.left
        root.left = None

        cur = root
        while cur.right:
            cur = cur.right
        cur.right = right

        self.flatten(root.right)
