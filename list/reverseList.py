from common.ListNode import *


# 206. 反转链表
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        while head:
            next = head.next
            head.next = dummy.next
            dummy.next = head
            head = next
        return dummy.next


if __name__ == '__main__':
    head = create_list_node([1, 2, 3, 4, 5])
    traverse(Solution().reverseList(head))
