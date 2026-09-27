class Solution:

    def pre(self, root, ma):
        if root is None:
            return 0

        count = 0

        if root.val >= ma:
            count = 1
            ma = root.val

        count += self.pre(root.left, ma)
        count += self.pre(root.right, ma)

        return count

    def goodNodes(self, root: TreeNode) -> int:
        return self.pre(root, root.val)