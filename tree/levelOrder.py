from common.TreeNode import *


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        path, ans = [], []
        queue = [root]
        while queue:
            for i in range(len(queue)):
                node = queue.pop(0)
                path.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(path[:])
            path.clear()
        return ans


if __name__ == '__main__':
    print(Solution().levelOrder(create_tree([1,2,3,4,5,6])))