from common.ListNode import *


# 445. 两数相加 II
class Solution:
    """
    递归创建
    """

    def reversed(self, head: ListNode, dummy=ListNode(0)):
        dummy = ListNode(0)
        tail = dummy
        while head:
            next_node = head.next
            head.next, tail.next = tail.next, head
            head = next_node
        return dummy.next

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1, l2 = self.reversed(l1), self.reversed(l2)
        return self.reversed(self.rec(l1, l2))

    def rec(self, l1: ListNode, l2: ListNode, bit=0) -> ListNode:
        if not l1 and not l2 and not bit:
            return None
        l1_val, l2_val = l1.val if l1 else 0, l2.val if l2 else 0
        l1_next, l2_next = l1.next if l1 else None, l2.next if l2 else None
        two_sum = l1_val + l2_val + bit
        return ListNode(two_sum % 10, self.rec(l1_next, l2_next, two_sum // 10))


if __name__ == '__main__':
    l1 = create_list_node([7, 1, 6])
    l2 = create_list_node([5, 9, 2])
    traverse(Solution().addTwoNumbers(l1, l2))
