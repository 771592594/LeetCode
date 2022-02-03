from typing import List

from common.TreeNode import TreeNode, traverse

BLACK, RED = 0, 1


class RedBlackTreeNode:

    def __init__(self, val=0, left=None, right=None, parent=None, color=BLACK):
        self.val: int = val
        self.left: RedBlackTreeNode = left
        self.right: RedBlackTreeNode = right
        self.parent: RedBlackTreeNode = parent
        self.color: int = color

    def __str__(self):
        return str(self.val)


class RedBlackTree:
    def __init__(self, arr: List[int]):
        self.root: RedBlackTreeNode = self.rec_create(arr, 0) if arr else None

    def rec_create(self, arr: List[int], i: int, parent: RedBlackTreeNode = None):
        if i >= len(arr) or arr[i] is None:
            return None
        node = RedBlackTreeNode(arr[i], None, None, parent, BLACK)
        node.left, node.right = self.rec_create(arr, i * 2 + 1, node), self.rec_create(arr, i * 2 + 2, node),
        return node


def left_rotate(tree: RedBlackTree, x: RedBlackTreeNode):
    """
    对红黑树的节点x进行左旋转
        px                             px
       /                              /
      x                              y
     / \       ----------->         / \
    lx  y                          x  ry
       / \                        / \
      ly ry                      lx ly

    :param tree:    红黑树
    :param x:       旋转的节点
    :return:        None
    """
    y: RedBlackTreeNode = x.right
    ly: RedBlackTreeNode = y.left
    px: RedBlackTreeNode = x.parent
    # y的左孩子设置为x的右孩子
    x.right = ly
    # y左孩子的父节点设置为x
    ly.parent = x
    # y的父节点设置为x的父节点
    y.parent = px
    # 如果x原来为树的根节点, 则将根节点修改为y
    if x.parent is None:
        tree.root = y
    # 如果x是其父节点左孩子, 则将y设置为x父节点的左孩子
    elif px.left == x:
        px.left = y
    # 如果x是其父节点的右孩子, 则将y设置为x父节点的右孩子
    else:
        px.right = y
    # y的左孩子设置为x
    y.left = x
    # x的父节点设置为y
    x.parent = y


def right_rotate(tree: RedBlackTree, y: RedBlackTreeNode):
    """
    对红黑树的节点y进行右旋转
          py                         py
         /                          /
        y                          x
       / \      ---------->       / \
      x  ry                      lx  y
     / \                            / \
    lx rx                          rx ry

    :param tree:    红黑树
    :param y:       旋转的节点
    :return:        None
    """

    x: RedBlackTreeNode = y.left
    rx: RedBlackTreeNode = x.right
    py: RedBlackTreeNode = y.parent
    # y的左孩子设置为x的右孩子
    y.left = rx
    # x的右孩子的父节点设置为y
    rx.parent = x
    # x的父节点设置为y的父节点
    x.parent = py
    # 如果y原来为树的根节点, 则将根节点修改为x
    if py is None:
        tree.root = x
    # 如果y是其父节点左孩子, 则将x设置为y父节点的左孩子
    elif py.left == y:
        py.left = x
    # 如果y是其父节点的右孩子, 则将x设置为y父节点的右孩子
    else:
        py.right = x
    # x的右孩子设置为y
    x.right = y
    # y的父节点设置为x
    y.parent = x


if __name__ == '__main__':
    # my_tree = RedBlackTree(['px', 'x', None, 'lx', 'y', None, None, None, None, 'ly', 'ry'])
    # node = my_tree.root.left
    # traverse(my_tree.root)
    # print("---------------------")
    # left_rotate(my_tree, node)
    # traverse(my_tree.root)

    my_tree = RedBlackTree(['py', 'y', None, 'x', 'ry', None, None, 'lx', 'rx', None, None])
    node = my_tree.root.left
    traverse(my_tree.root)
    print("---------------------")
    right_rotate(my_tree, node)
    traverse(my_tree.root)
