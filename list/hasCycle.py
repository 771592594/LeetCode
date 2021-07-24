from common.ListNode import *


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow, fast = head, head
        while slow and fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow == fast:
                return True
        return False
