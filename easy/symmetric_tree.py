# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorder_traverse(self, root, parent=0):
        if not root:
            return []
        return self.inorder_traverse(root.left, -1) + [(root.val, parent)] + self.inorder_traverse(root.right, 1)

    def isSymmetric(self, root: TreeNode) -> bool:
        left, right = self.inorder_traverse(root.left), self.inorder_traverse(root.right)
        return left == [(val, -side) for val, side in right[::-1]]


if __name__ == '__main__':
    r = TreeNode(1)
    r.left = TreeNode(2)
    r.left.left = TreeNode(2)
    # r.left.right = TreeNode(3)
    r.right = TreeNode(2)
    # r.right.left = TreeNode(2)
    r.right.right = TreeNode(2)
    print(Solution().isSymmetric(r))
