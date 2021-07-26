from common.ListNode import *


# 141. 环形链表
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow, fast = head, head
        while slow and fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow == fast:
                return True
        return False
