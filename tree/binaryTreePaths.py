# 257. 二叉树的所有路径
from typing import List

from common.TreeNode import TreeNode


# 257. 二叉树的所有路径
class Solution:
    """
    前序遍历 + 回溯算法
    """

    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        def toStr(path: List[int]):
            s = ''
            for idx, val in enumerate(path):
                s += f"->{str(val)}" if idx else str(val)
            return s

        def prev(node, path: List[int]):
            path.append(node.val)
            if not node.left and not node.right:
                paths.append(path[:])
                path.pop()
                return
            if node.left:
                prev(node.left, path)
            if node.right:
                prev(node.right, path)
            path.pop()

        paths = []
        prev(root, [])
        return list(map(toStr, paths))


if __name__ == '__main__':
    node = TreeNode(0)
    node.left = TreeNode(1)
    print(Solution().binaryTreePaths(node))
