from common.ListNode import *


# 24. 两两交换链表中的节点
class Solution:
    def rec(self, node: ListNode):
        if node and node.next and node.next.next:
            temp = node.next
            node.next = temp.next
            temp.next = node.next.next
            node.next.next = temp
            self.rec(node.next.next)

    def swapPairs(self, head: ListNode) -> ListNode:
        pre = ListNode(0, head)
        self.rec(pre)
        return pre.next


if __name__ == '__main__':
    show(Solution().swapPairs(create_list_node([1, 2, 3, 4])))
