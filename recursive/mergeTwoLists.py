from common.ListNode import *


# 21. 合并两个有序链表
class Solution:
    def rec(self, l1: ListNode, l2: ListNode, ret: ListNode):
        if not l1 and not l2:
            return
        if not l1:
            ret.next = l2
            return
        if not l2:
            ret.next = l1
            return
        if l1.val < l2.val:
            ret.next = l1
            l1 = l1.next
        else:
            ret.next = l2
            l2 = l2.next
        self.rec(l1, l2, ret.next)

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        ret = ListNode(0)
        self.rec(l1, l2, ret)
        return ret.next

if __name__ == '__main__':
    li = Solution().mergeTwoLists(
        create_list_node([1, 2, 4]),
        create_list_node([1, 3, 4])
    )
    show(li)
