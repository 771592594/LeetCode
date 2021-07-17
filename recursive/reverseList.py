from common.ListNode import *


class Solution:
    def rec(self, node: ListNode, temp: ListNode):
        if not node:
            return
        next = node.next
        node.next = temp.next
        temp.next = node
        self.rec(next, temp)

    def reverseList(self, head: ListNode) -> ListNode:
        temp = ListNode(0)
        self.rec(head, temp)
        return temp.next


if __name__ == '__main__':
    show(Solution().reverseList(create_list_node([1, 2, 3, 4, 5])))
