# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode], higher_bound = float('+inf'), lower_bound = float('-inf')) -> bool:
        if root is None:
            return True

        if not (lower_bound < root.val < higher_bound):
            return False

            
        return self.isValidBST(root.left, root.val, lower_bound) and self.isValidBST(root.right, higher_bound, root.val)