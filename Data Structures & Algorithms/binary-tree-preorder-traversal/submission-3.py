# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def pre(self,l,root:Optional[TreeNode]) -> None:
        if root is None:
            return 
        l.append(root.val)
        self.pre(l,root.left)
        self.pre(l,root.right)
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        l=[]
        self.pre(l,root)
        return l
        