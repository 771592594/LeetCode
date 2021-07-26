from common.ListNode import *


# 61. 旋转链表
class Solution:
    """
    快慢指针 环路分割
    """
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head
        # 求出链表长度
        node, length = head, 1
        while node.next:
            node, length = node.next, length + 1
        # 对k取余，求有效移动次数
        k = k % length
        # 通过快慢指针找到倒数第 k + 1 的位置
        fast, slow = head, head
        while k:
            fast, k = fast.next, k - 1
        while fast.next:
            fast, slow = fast.next, slow.next
        # 将链表头尾相连形成环路
        fast.next = head
        # 在倒数第 k + 1 的位置断开，它的原后继节点就是旋转后的起始位置
        ret, slow.next = slow.next, None
        return ret


if __name__ == '__main__':
    traverse(Solution().rotateRight(create_list_node([1, 2, 3, 4]), 1))
