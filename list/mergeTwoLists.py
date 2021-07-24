from common.ListNode import *


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        v_head = ListNode(0)
        temp = v_head
        while l1 and l2:
            if l1.val < l2.val:
                temp.next = l1
                l1 = l1.next
            else:
                temp.next = l2
                l2 = l2.next
            temp = temp.next
        temp.next = l1 if l1 else l2
        return v_head.next


if __name__ == '__main__':
    head1 = create_list_node([1, 4, 5])
    head2 = create_list_node([2, 3, 6])
    traverse(Solution().mergeTwoLists(head1, head2))
