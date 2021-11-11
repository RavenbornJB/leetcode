from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode], min_value=-float('inf'), max_value=float('inf')) -> bool:
        if not root:
            return True

        if not min_value < root.val < max_value:
            return False

        if not self.isValidBST(root.left, min_value, root.val):
            return False
        if not self.isValidBST(root.right, root.val, max_value):
            return False

        return True
