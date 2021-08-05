from common.TreeNode import *


# 1022. 从根到叶的二进制数之和
class Solution:
    """
    从根到叶的二进制数之和 = 左子树的二进制数之和 + 右子树的二进制数之和
    """
    def sumRootToLeaf(self, root: TreeNode) -> int:
        def getSum(path: List[int]):
            ret = 0
            for i in path:
                ret = ret * 2 + i
            return ret

        def backtrack(node: TreeNode, path: List[int]):
            if not node:
                return 0
            path.append(node.val)
            if not node.left and not node.right:
                ret = getSum(path)
            else:
                ret = backtrack(node.left, path) + backtrack(node.right, path)
            path.pop()
            return ret

        return backtrack(root, [])


if __name__ == '__main__':
    t = create_tree([1, 0, 1, 0, 1, 0, 1])
    print(Solution().sumRootToLeaf(t))
