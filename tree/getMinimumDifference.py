# 530. 二叉搜索树的最小绝对差
import sys

from common.TreeNode import *


class Solution:
    """
    中序遍历转有序数组，然后计算相邻节点差值的绝对值的最小值
    """

    def getMinimumDifference(self, root: TreeNode) -> int:
        def inorder(node: TreeNode):
            if not node:
                return
            inorder(node.left)
            values.append(node.val)
            inorder(node.right)
        values = []
        inorder(root)
        minimum = sys.maxsize
        for i in range(1, len(values)):
            minimum = min(minimum, values[i] - values[i-1])
        return minimum
