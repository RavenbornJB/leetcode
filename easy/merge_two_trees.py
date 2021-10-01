# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 and root2:
            root = TreeNode(root1.val + root2.val)
            root.left = self.mergeTrees(root1.left, root2.left)
            root.right = self.mergeTrees(root1.right, root2.right)
            return root
        return root1 or root2


if __name__ == '__main__':
    r = TreeNode(1)
    r.left = TreeNode(2)
    r.left.left = TreeNode(4)
    r.left.right = TreeNode(5)
    r.right = TreeNode(3)
    # r.right.left = TreeNode(2)
    # r.right.right = TreeNode(2)
    print(Solution().mergeTrees(r, None).left.val)
