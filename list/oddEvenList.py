from common.ListNode import *


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        cnt = 1
        odd_dummy, even_dummy = ListNode(0), ListNode(0)
        odd_last, even_last = odd_dummy, even_dummy
        while head:
            if cnt & 1:
                odd_last.next = head
                odd_last = odd_last.next
            else:
                even_last.next = head
                even_last = even_last.next
            head, cnt = head.next, cnt + 1
        odd_last.next, even_last.next = even_dummy.next, None
        return odd_dummy.next


if __name__ == '__main__':
    traverse(Solution().oddEvenList(create_list_node([2, 3, 4, 5, 6])))
