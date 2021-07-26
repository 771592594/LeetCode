from common.ListNode import *


class Solution:
    # 面试题 02.03. 删除中间节点
    """
    后继节点复制
    """
    def deleteNode(self, node: ListNode):
        node.val, node.next = node.next.val, node.next.next

    # 剑指 Offer 18. 删除链表的节点
    """
    遍历删除
    """
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(0, head)
        node = dummy
        while node.next:
            if node.next.val == val:
                node.next = node.next.next
            else:
                node = node.next
        return dummy.next


if __name__ == '__main__':
    traverse(Solution().deleteNode(create_list_node([1, 1, 2, 3, 4]), 1))
