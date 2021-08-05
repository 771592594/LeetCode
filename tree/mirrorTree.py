from common.TreeNode import *


# 剑指 Offer 27. 二叉树的镜像
class Solution:
    """
    创建节点，然后递归创建左右孩子
    由于是镜像，所以创建的左孩子是原树的右孩子；创建的右孩子是原树的左孩子
    """
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        return TreeNode(root.val, self.mirrorTree(root.right), self.mirrorTree(root.left)) if root else root
