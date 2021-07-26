class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next


# 剑指 Offer 35. 复杂链表的复制
class Solution:
    """
    递归 + 哈希表
    遍历原链表，创建新节点, 建立<原节点, 新节点>的字典
    递归创建原节点的 next 和 random,
    从字典中查找节点是否被已创建，如果已经创建则直接拿来使用
    """

    def rec(self, head: 'Node', created: dict):
        if not head:
            return None
        if node := created.get(head):
            return node
        node = Node(head.val)
        created[head] = node
        node.next = self.rec(head.next, created)
        node.random = self.rec(head.random, created)
        return node

    def copyRandomList(self, head: 'Node') -> 'Node':
        return self.rec(head, dict())
