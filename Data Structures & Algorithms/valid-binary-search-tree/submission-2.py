class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.prev = None
        def in_order(root):
            if root is None:
                return True
            if not in_order(root.left):
                return False
            if self.prev is not None and root.val <= self.prev:
                return False
            self.prev = root.val
            return in_order(root.right)
        return in_order(root)