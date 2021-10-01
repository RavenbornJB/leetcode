# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def depth_and_diameter(self, root):
        if not root:
            return 0, 0

        ldep, ldia = self.depth_and_diameter(root.left)
        rdep, rdia = self.depth_and_diameter(root.right)

        return max(ldep, rdep) + 1, max(ldia, rdia, ldep + rdep)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return self.depth_and_diameter(root)[1]


if __name__ == '__main__':
    r = TreeNode(1)
    r.left = TreeNode(2)
    r.left.left = TreeNode(4)
    r.left.right = TreeNode(5)
    r.right = TreeNode(3)
    # r.right.left = TreeNode(2)
    # r.right.right = TreeNode(2)
    print(Solution().diameterOfBinaryTree(r))
