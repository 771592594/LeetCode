from common.TreeNode import TreeNode


# 226. 翻转二叉树
class Solution:
    """
    前序或后序遍历节点，并交换左右孩子
    中序遍历，只能实现根节点的左子树的反转，效果如下：
            1
        2       3
      4   5   6   7
    反转后：
            1
        3       2
     6    7   5   4
    """
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
