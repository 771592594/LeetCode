from common.ListNode import *


class Solution:
    # 203. 移除链表元素
    """
    虚拟头节点 + 前驱节点
    """
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(0, head)
        prev = dummy
        while prev.next:
            if prev.next.val == val:
                prev.next = prev.next.next
            else:
                prev = prev.next
        return dummy.next

    """
    插入法
    将不满足 node.val = val 的节点插入到新链表中
    """
    # todo 博客上有错误
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(0, head)
        tail, node = dummy, head
        while node:
            next_node = node.next
            if node.val != val:
                tail.next = node
                tail = node
            node = next_node
        # 清除尾节点的后继
        tail.next = None
        return dummy.next


if __name__ == '__main__':
    traverse(Solution().removeElements(create_list_node([1, 1, 2, 3, 4, 1]), 1))
