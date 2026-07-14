# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        self.max_ever = root.val
        
        self.maxSum(root)

        return self.max_ever


    def maxSum(self, root):
        if root is None:
            return 0
        current_max = root.val

        
        left = max(0, self.maxSum(root.left))
        right = max(0, self.maxSum(root.right))

        root_sum = root.val + left + right

        current_max = max(current_max, root_sum) if root.left or root.right else root.val

        self.max_ever = max(self.max_ever, current_max)

        return root.val + max(left, right)



        
        