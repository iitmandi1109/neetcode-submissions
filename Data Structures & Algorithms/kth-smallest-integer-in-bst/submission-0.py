# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        l=[]
        def ino(root,l):
            if root ==None : return None
            ino(root.left,l)
            l.append(root.val)
            ino(root.right,l)
            return l
        ino(root,l)
        return l[k-1]