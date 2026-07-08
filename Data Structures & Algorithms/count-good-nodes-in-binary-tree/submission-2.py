# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode, biggest_node = None) -> int:
        if root is None:
            return 0

        if biggest_node is None:
            biggest_node = root.val
        
        if root.val >= biggest_node:
            return 1 + self.goodNodes(root.left, root.val) + self.goodNodes(root.right, root.val)  

        return self.goodNodes(root.left, biggest_node) + self.goodNodes(root.right, biggest_node)