# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def depth(self, root):
        if not root:
            return 0
        left = self.depth(root.left)
        right = self.depth(root.right)
        if abs(left - right) > 1:
            raise ValueError("depth diff too large")
        return max(left, right) + 1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        try:
            self.depth(root)
        except ValueError as e:
            if str(e) == "depth diff too large":
                return False
        return True


if __name__ == '__main__':
    r = TreeNode(3)
    r.left = TreeNode(4)
    r.left.left = TreeNode(1)
    r.left.right = TreeNode(2)
    # r.right = TreeNode(5)
    print(Solution().isBalanced(r))
