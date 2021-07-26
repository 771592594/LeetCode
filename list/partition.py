from common.ListNode import *


# 面试题 02.04. 分割链表
class Solution:
    """
    分割 + 合并
    新建两个链表ge和lt
    遍历输入的链表，将值大于等于x的节点尾插到ge链表中，将值小于x的节点尾插到lt链表
    最后拼接链表 lt->ge
    """
    def partition(self, head: ListNode, x: int) -> ListNode:
        ge_dummy, lt_gummy = ListNode(0), ListNode(0)
        ge_last, lt_last = ge_dummy, lt_gummy
        while head:
            if head.val >= x:
                ge_last.next = head
                ge_last = ge_last.next
            else:
                lt_last.next = head
                lt_last = lt_last.next
            head = head.next
        lt_last.next, ge_last.next = ge_dummy.next, None
        return lt_gummy.next


if __name__ == '__main__':
    li = create_list_node([6, 5, 4, 3, 2, 1])
    traverse(Solution().partition(li, 3))

