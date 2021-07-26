from common.ListNode import *


# 876. 链表的中间结点
class Solution:
    """
    快慢指针：
    快慢指针从头节点出发，慢指针每次走一步，快指针每次走两步
    当快指针无法继续走下取的时候，慢指针就走到了中间节点的前驱
    TIP: 对于长度为偶数的链表，中间节点是中间的第二个节点
    """

    def middleNode(self, head: ListNode) -> ListNode:
        slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        return slow


if __name__ == '__main__':
    print(Solution().middleNode(create_list_node([1, 2, 3, 4, 5])))
    print(Solution().middleNode(create_list_node([1, 2, 3, 4, 5, 6])))
