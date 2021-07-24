from random import randint

from common.ListNode import *


class Solution:

    def __init__(self) -> None:
        self.sort = self.insertSort

    # 冒泡排序
    def bubbleSort(self, head: ListNode) -> ListNode:
        if not head:
            return head
        getLen = lambda node: 1 + getLen(node.next) if node else 0
        temp, length = head, getLen(head)
        # 排序次数为 length - 1 次
        for i in range(length - 1):
            # 每趟排序交换次数为 length - i - 1
            for _ in range(length - i - 1):
                if temp.val > temp.next.val:
                    temp.val, temp.next.val = temp.next.val, temp.val
                temp = temp.next
            temp = head
        return head

    # 选择排序
    def selectSort(self, head: ListNode) -> ListNode:
        if not head:
            return head
        cur = head
        while cur.next:
            mini_node, node = cur, cur.next
            while node:
                mini_node = node if node.val < mini_node.val else mini_node
                node = node.next
            cur.val, mini_node.val = mini_node.val, cur.val
            cur = cur.next
        return head

    # 插入排序
    def insertSort(self, head: ListNode) -> ListNode:
        if not head:
            return head
        dummy = ListNode(0, head)
        curr, last = head.next, head
        while curr:
            # 如果当前元素不小于最后插入的元素，说明该元素位置正确
            if curr.val >= last.val:
                last = last.next
            # 否则从头开始遍历，找到正确的位置并插入
            else:
                prev = dummy
                while curr.val >= prev.next.val:
                    prev = prev.next
                curr.next, prev.next, last.next = prev.next, curr, curr.next
            curr = last.next
        return dummy.next

    # 归并排序
    def mergeSort(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        # 通过快慢指针找到链表的中间节点
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # 通过中间节点，将链表一分为二
        l1, l2 = head, slow.next
        slow.next = None
        l1 = self.mergeSort(l1)
        l2 = self.mergeSort(l2)
        # 将两个链表归并为一个有序列表
        dummy = ListNode(0)
        temp = dummy
        while l1 and l2:
            if l1.val < l2.val:
                temp.next, l1 = l1, l1.next
            else:
                temp.next, l2 = l2, l2.next
            temp = temp.next
        temp.next = l1 if l1 else l2
        return dummy.next


if __name__ == '__main__':
    # arr = [4, 2, 1, 3]
    arr = [randint(0, 100) for _ in range(10)]
    traverse(Solution().sort(create_list_node(arr)))
