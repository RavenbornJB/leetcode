# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSame(self, root1, root2):
        if not (root1 and root2):
            return root1 is root2

        return root1.val == root2.val and self.isSame(root1.left, root2.left) and self.isSame(root1.right, root2.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if self.isSame(root, subRoot):
            return True

        if not root:
            return False

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


if __name__ == '__main__':
    r = TreeNode(3)
    # r.left = TreeNode(4)
    # r.left.left = TreeNode(1)
    # r.left.right = TreeNode(2)
    # r.right = TreeNode(5)
    sr = TreeNode(3)
    # sr.left = TreeNode(1)
    # sr.right = TreeNode(2)
    print(Solution().isSubtree(r, sr))
