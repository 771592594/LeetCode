from typing import List

from common.TreeNode import traverse

BLACK, RED = 0, 1


class RedBlackTreeNode:

    def __init__(self, val=0, left=None, right=None, parent=None, color=RED):
        self.val: int = val
        self.left: RedBlackTreeNode = left
        self.right: RedBlackTreeNode = right
        self.parent: RedBlackTreeNode = parent
        self.color: int = color

    def __str__(self):
        return str(self.val)


class RedBlackTree:
    def __init__(self, arr=None):
        if arr is None:
            arr = []
        self.root: RedBlackTreeNode = self.__create(arr, 0) if arr else None

    def __create(self, arr: List[int], i: int, parent: RedBlackTreeNode = None):
        if not arr or i >= len(arr) or arr[i] is None:
            return None
        node = RedBlackTreeNode(arr[i], None, None, parent, RED)
        node.left, node.right = self.__create(arr, i * 2 + 1, node), self.__create(arr, i * 2 + 2, node),
        return node

    def add(self, val: int):
        if not self.root:
            self.root = RedBlackTreeNode(val=val, parent=None, color=BLACK)
            return None
        # 确定插入的位置
        node, parent = self.root, self.root
        while node:
            parent = node
            if val <= node.val:
                node = node.left
            else:
                node = node.right
        # 如果插入的节点比父节点小, 则作为左孩子; 否则作为右孩子
        new_node = RedBlackTreeNode(val=val, parent=parent, color=RED)
        if val <= parent.val:
            parent.left = new_node
        else:
            parent.right = new_node
        # 如果父节点也是红色, 插入后就会破坏红黑树的性质, 因此需要重新修复
        self.__insert_fixup(new_node)

    def __insert_fixup(self, node: RedBlackTreeNode):
        """
        插入新节点后修复红黑树
        :param node:        新插入的节点
        :return:            None
        """
        while node.parent and node.parent.color == RED:
            parent, grand_parent = node.parent, node.parent.parent
            # 若node的父节点是node的祖父节点的左孩子
            if not grand_parent:
                return None
            if parent == grand_parent.left:
                uncle = grand_parent.right
                # case 1: 叔叔节点是红色
                if uncle and uncle.color == RED:
                    parent.color, uncle.color = BLACK, BLACK
                    grand_parent.color = RED
                    node = grand_parent
                # case 2: 叔叔节点是黑色, 当前节点是右孩子
                elif node == parent.right:
                    node = parent
                    left_rotate(self, node)
                # case 3: 叔叔节点是黑色, 当前节点是左孩子
                else:
                    parent.color = BLACK
                    grand_parent.color = RED
                    right_rotate(self, grand_parent)
            # 若node的父节点是node的祖父节点的右孩子
            else:
                uncle = grand_parent.left
                # case 1: 叔叔节点是红色
                if uncle and uncle.color == RED:
                    parent.color, uncle.color = BLACK, BLACK
                    grand_parent.color = RED
                    node = grand_parent
                # case 2: 叔叔节点是黑色, 当前节点是右孩子
                elif node == parent.left:
                    node = parent
                    right_rotate(self, node)
                # case 3: 叔叔节点是黑色, 当前节点是左孩子
                else:
                    parent.color = BLACK
                    grand_parent.color = RED
                    left_rotate(self, grand_parent)


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
    if ly:
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
    # y的左孩子设置为x, x的父节点设置为y
    y.left, x.parent = x, y


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
    if rx:
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
    # x的右孩子设置为y, y的父节点设置为x
    x.right, y.parent = y, x


if __name__ == '__main__':
    my_tree = RedBlackTree()
    for i in [3, 5, 7, 1, 2, 4]:
        my_tree.add(i)
    traverse(my_tree.root)

    # my_tree = RedBlackTree(['px', 'x', None, 'lx', 'y', None, None, None, None, 'ly', 'ry'])
    # node = my_tree.root.left
    # traverse(my_tree.root)
    # print("---------------------")
    # left_rotate(my_tree, node)
    # traverse(my_tree.root)

    # my_tree = RedBlackTree(['py', 'y', None, 'x', 'ry', None, None, 'lx', 'rx', None, None])
    # my_node = my_tree.root.left
    # traverse(my_tree.root)
    # print("---------------------")
    # right_rotate(my_tree, my_node)
    # traverse(my_tree.root)
