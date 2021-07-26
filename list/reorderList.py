from common.ListNode import *


# 143. 重排链表
class Solution:
    def reorderList(self, head: ListNode) -> None:
        if not head or not head.next:
            return
        slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        l1, l2, mid = head, slow, slow
        # 反转l2
        dummy = ListNode(0)
        while l2:
            temp = l2.next
            l2.next = dummy.next
            dummy.next = l2
            l2 = temp
        l2 = dummy.next
        # 将l2插入l1
        while l1 and l1.next != mid:
            l1_next, l2_next = l1.next, l2.next
            l1.next, l2.next = l2, l1_next
            l1, l2 = l1_next, l2_next
        l1.next = l2


if __name__ == '__main__':
    l1 = create_list_node([1, 2, 3, 4, 5])
    Solution().reorderList(l1)
    traverse(l1)
    l2 = create_list_node([1, 2, 3, 4, 5, 6])
    Solution().reorderList(l2)
    traverse(l2)
