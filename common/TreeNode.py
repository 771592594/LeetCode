from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return str(self.val)


def traverse(node):
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
                queue.append(node.left)
                queue.append(node.right)
            print(str(node), end=" ")
        print()


def create_tree(arr: List[int]):
    def rec_create(i):
        if i >= len(arr) or arr[i] is None:
            return None
        node = TreeNode(arr[i], None, None)
        node.left, node.right = rec_create(i * 2 + 1), rec_create(i * 2 + 2)
        return node

    return rec_create(0) if arr else None


if __name__ == '__main__':
    root = create_tree([1, 2, 3, 4, 5, 6, 7])
    traverse(root)
