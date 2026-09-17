# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def height(self,root: Optional[TreeNode]) -> int:
        if root==None: return 0
        return 1+max(self.height(root.left),self.height(root.right))

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        left_height = self.height(root.left)
        right_height = self.height(root.right)

        diameter = left_height + right_height

        return max(
            diameter,
            self.diameterOfBinaryTree(root.left),
            self.diameterOfBinaryTree(root.right)
        )

        