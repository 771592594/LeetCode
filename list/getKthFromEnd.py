from common.ListNode import *


class Solution:
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
