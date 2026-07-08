# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        self.balanced = True

        self.depth(root)

        return self.balanced

    def depth(self, root):
        if root is None:
            return 0

        left_depth = self.depth(root.left)
        right_depth = self.depth(root.right)

        if left_depth == right_depth and self.balanced == True:
            self.balanced = True
        elif left_depth + 1 == right_depth and self.balanced == True:
            self.balanced = True
        elif left_depth == right_depth + 1 and self.balanced == True:
            self.balanced = True
        else:
            self.balanced = False

        return 1 + max(left_depth, right_depth)