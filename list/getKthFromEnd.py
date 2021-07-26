from common.ListNode import *


# 剑指 Offer 22. 链表中倒数第k个节点
class Solution:
    """
    快慢指针：
    快指针先走 k -1 步，然后快慢指针同步走
    当快指针走到最后一个节点时，慢指针当好位于倒数第K个节点
    """
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        slow, fast = head, head
        for i in range(k - 1):
            fast = fast.next
        while fast.next:
            slow = slow.next
            fast = fast.next
        return slow


if __name__ == '__main__':
    head = create_list_node([1, 2, 3, 4, 5])
    print(Solution().getKthFromEnd(head, 1).val)
