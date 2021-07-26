from common.ListNode import *


# 19. 删除链表的倒数第 N 个结点
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)
        slow, fast = dummy, dummy
        while n:
            fast, n = fast.next, n - 1
        while fast.next:
            slow, fast = slow.next, fast.next
        slow.next = slow.next.next
        return dummy.next
