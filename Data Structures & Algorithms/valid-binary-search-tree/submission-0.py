class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        r = []
        def inorderTraversal(root):
            if not root:
                return []
            inorderTraversal(root.left)
            r.append(root.val)
            inorderTraversal(root.right)
        inorderTraversal(root)
        for i in range(1, len(r)):
            if r[i] <= r[i - 1]:
                return False
        return True