from common.TreeNode import TreeNode


# 235. 二叉搜索树的最近公共祖先
class Solution:
    """
    如果 p,q 一个比根节点大，一个比根节点小，那么它们在根的两侧，最近公共祖先为根节点
    如果 p,q 其中一个为根节点，那么它们的最近公共祖先就是根节点
    如果 p,q 在根节点的同一侧，那么就递归遍历该侧的节点，重复上述判断
    """
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # p,q 分布在根的两侧 或 p,q 中存在根节点
        if (p.val - root.val) * (q.val - root.val) <= 0:
            return root
        # p,q 在同一侧
        if p.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return self.lowestCommonAncestor(root.right, p, q)
