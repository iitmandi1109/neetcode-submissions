# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        l=[]
        def ino(l,root):
            if root==None: return None
            ino(l,root.left)
            l.append(root.val)
            ino(l,root.right)
            return l
        ino(l,root)
        for i in range(1,len(l)):
            if  l[i-1]>=l[i]: return False  
        return True     