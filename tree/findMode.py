# 501. 二叉搜索树中的众数
from common.TreeNode import *


class Solution:
    """
    前序遍历
    """
    def findMode(self, root: TreeNode) -> List[int]:
        def prev(node: TreeNode):
            if not node:
                return
            count_dict.setdefault(node.val, 0)
            count_dict[node.val] += 1
            prev(node.left)
            prev(node.right)

        if not root:
            return []
        count_dict = {}
        prev(root)
        maximum = max(count_dict.values())
        ans = [k for k, v in count_dict.items() if v == maximum]
        return ans


if __name__ == '__main__':
    t = create_tree([1, None, 2])
    t.right.right = TreeNode(2)
    print(Solution().findMode(t))
