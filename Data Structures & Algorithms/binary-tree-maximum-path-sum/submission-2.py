# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = root.val

        self.maxDiameter(root)

        return self.max_sum

    def maxDiameter(self, root):
        if root is None:
            return 0
        
        left_max = self.maxDiameter(root.left)
        right_max = self.maxDiameter(root.right)

        if left_max <= 0 and right_max <= 0:
            current_max = root.val
        else:
            current_max = root.val + max(left_max, right_max)

        if left_max <= 0 or right_max <= 0:
            self.max_sum = max(self.max_sum, current_max)
        else:
            self.max_sum = max(self.max_sum, root.val + right_max + left_max)
            
        return current_max