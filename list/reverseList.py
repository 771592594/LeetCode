from common.ListNode import *


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        v_head = ListNode(0)
        while head:
            next = head.next
            head.next = v_head.next
            v_head.next = head
            head = next
        return v_head.next


if __name__ == '__main__':
    head = create_list_node([1, 2, 3, 4, 5])
    traverse(Solution().reverseList(head))
