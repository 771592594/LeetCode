from common.ListNode import *


# 2. 两数相加
class Solution:
    def rec(self, l1: ListNode, l2: ListNode, bit: int) -> ListNode:
        if not (l1 or l2 or bit):
            return None
        v1, v2 = l1.val if l1 else 0, l2.val if l2 else 0
        sum = v1 + v2 + bit
        mod, bit = sum % 10, sum // 10
        node = ListNode(mod)
        l1, l2 = l1.next if l1 else None, l2.next if l2 else None
        node.next = self.rec(l1, l2, bit)
        return node

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        return self.rec(l1, l2, 0)


if __name__ == '__main__':
    l1 = create_list_node([9, 9, 9, 9, 9, 9, 9])
    l2 = create_list_node([9, 9, 9, 9])
    show(l1)
    show(l2)
    show(Solution().addTwoNumbers(l1, l2))
