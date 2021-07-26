from common.ListNode import *


# 83. 删除排序链表中的重复元素
class Solution:
    """
    插入排序
    因为链表是有序的，可以利用插入排序的思想
    将原链表中的元素不重复地插入新链表中
    """

    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        curr, tail = head.next, head
        while curr:
            if curr.val > tail.val:
                tail.next = curr
                tail = curr
            curr = curr.next
        # 清除尾节点的后继
        tail.next = None
        return head


if __name__ == '__main__':
    l1 = create_list_node([1, 1, 2, 3, 3])
    traverse(Solution().deleteDuplicates(l1))
