from common.TreeNode import *


# 剑指 Offer 28. 对称的二叉树
class Solution:
    """
    对称遍历
    """
    def isSymmetric(self, root: TreeNode) -> bool:
        def rec(p: TreeNode, q: TreeNode):
            if not p or not q:
                return p == q
            return p.val == q.val and rec(p.left, q.right) and rec(p.right, q.left)
        return rec(root, root)


if __name__ == '__main__':
    print(Solution().isSymmetric(create_tree([1, 2, 3])))
