# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        self.d_list = []
        self.preorder(root)

        return ','.join(self.d_list)
        
    def preorder(self, root):
        if root is None:
            self.d_list.append("N")
            return

        self.d_list.append(f"{root.val}")
        self.preorder(root.left)
        self.preorder(root.right)

        return


    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return []

        self.values = iter(data.split(','))

        return self.buildTree()
        
    def buildTree(self):
        val = next(self.values)

        if val == "N":
            return None

        root = TreeNode(val)
        root.left = self.buildTree()
        root.right = self.buildTree()

        return root


        
    