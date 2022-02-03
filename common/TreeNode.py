from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return str(self.val)


def traverse(node: TreeNode):
    if not node:
        print([])
    queue = [node]
    while queue:
        nodes = []
        count = len(queue)
        for i in range(count):
            node = queue.pop(0)
            nodes.append(node)
            if node:
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            print(node, end=" ")
        print()


def create_tree(arr: List[int]):
    def rec_create(i):
        if i >= len(arr) or arr[i] is None:
            return None
        if i in node_dict:
            return node_dict[i]
        node = TreeNode(arr[i], rec_create(i * 2 + 1), rec_create(i * 2 + 2))
        node_dict[i] = node
        return node

    if not arr:
        return None
    node_dict = {}
    for idx, num in enumerate(arr):
        rec_create(idx)
    return node_dict[0]


if __name__ == '__main__':
    root = create_tree([1, 2, 3, 4, 5, 6, 7])
    traverse(root)
