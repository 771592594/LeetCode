from common.TreeNode import TreeNode


# 404. 左叶子之和
class Solution:
    """
    根节点的左孩子之和 = 左子树的左孩子之和 + 右子树的左孩子之和
    """
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        def rec(node, is_left):
            if not node:
                return 0
            if is_left and not node.left and not node.right:
                return node.val
            return rec(node.left, 1) + rec(node.right, 0)
        return rec(root, 0)
