from common.ListNode import *


# 1721. 交换链表中的节点
class Solution:
    """
    快慢指针：
    通过快慢指针定位倒数第K个节点
    从头遍历链表，定义第K个节点
    交换这两个节点的值
    """
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        if not head.next:
            return head
        k = k - 1
        slow, fast = head, head
        while k:
            fast, k = fast.next, k - 1
        front = fast
        while fast.next:
            slow, fast = slow.next, fast.next
        front.val, slow.val = slow.val, front.val
        return head


if __name__ == '__main__':
    traverse(Solution().swapNodes(create_list_node([1,2,3]), 2))
