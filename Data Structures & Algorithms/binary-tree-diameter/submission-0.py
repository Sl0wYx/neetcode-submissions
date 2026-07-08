# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_depth = 0
        self.depth(root)

        return self.max_depth

    def depth(self, node):
        if node is None:
            return 0

        right_depth = self.depth(node.right)
        left_depth = self.depth(node.left)

        self.max_depth = max(self.max_depth, right_depth + left_depth)
        return 1 + max(left_depth, right_depth)

        