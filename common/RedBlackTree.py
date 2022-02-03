from typing import List

from common.TreeNode import TreeNode, traverse

BLACK, RED = 0, 1


class RedBlackTreeNode(TreeNode):

    def __init__(self, val=0, left=None, right=None, parent=None, color=BLACK):
        super().__init__(val, left, right)
        self.color = color
        self.parent = parent


def create_tree(arr: List[int]):
    def rec_create(i: int, parent: RedBlackTreeNode = None):
        if i >= len(arr) or arr[i] is None:
            return None
        node = RedBlackTreeNode(arr[i], None, None, parent, BLACK)
        node.left, node.right = rec_create(i * 2 + 1, node), rec_create(i * 2 + 2, node),
        return node

    return rec_create(0) if arr else None


if __name__ == '__main__':
    root = create_tree([1, 2, 3, 4, 5, 6, 7])
    traverse(root)
