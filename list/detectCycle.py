from common.ListNode import *


# 142. 环形链表 II
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow, fast = head, head
        while slow and fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow == fast:
                while slow != head:
                    slow, head = slow.next, head.next
                return slow
        return None