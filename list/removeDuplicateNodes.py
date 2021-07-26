from common.ListNode import *


# 面试题 02.01. 移除重复节点
class Solution:
    """
    Map
    """
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        # 链表节点个数小于2，那么不存在重复节点
        if not head or not head.next:
            return head
        map = dict()
        # 遍历节点，若节点值不在集合中，则加入集合；否则删除该节点
        node = head
        while node.next:
            map[node.val] = 1
            if map.get(node.next.val):
                node.next = node.next.next
            else:
                node = node.next
        return head


if __name__ == '__main__':
    traverse(Solution().removeDuplicateNodes(create_list_node([1, 2, 2, 3, 1, 4, 5])))
