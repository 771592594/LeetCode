from common.ListNode import *


class Solution:
    def rec(self, node: ListNode):
        if node and node.next and node.next.next:
            a, b = node.next, node.next.next
            node.next, a.next, b.next = b, b.next, a
            self.rec(node.next.next)

    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(0, head)
        self.rec(dummy)
        return dummy.next


if __name__ == '__main__':
    traverse(Solution().swapPairs(create_list_node([1, 2, 3, 4])))
