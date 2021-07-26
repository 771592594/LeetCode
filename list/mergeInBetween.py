from common.ListNode import *


# 1669. 合并两个链表
class Solution:
    """
    链表分割 + 拼接
    遍历list1找到第a-1个节点A和第b+1个节点B（本题目索引从0开始）
    拼接链表：A->list2->B
    """
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        temp, b = list1, b + 1
        pre_a, pre_b = None, None
        while not pre_a or not pre_b:
            a, b = a - 1, b - 1
            if not a:
                pre_a = temp
            if not b:
                pre_b = temp
                break
            temp = temp.next
        pre_a.next = list2
        last = list2
        while last.next:
            last = last.next
        last.next = pre_b.next
        return list1


if __name__ == '__main__':
    l1 = create_list_node([0, 1, 2, 3, 4, 5])
    l2 = create_list_node([1000000, 1000001, 1000002])
    traverse(Solution().mergeInBetween(l1, 3, 4, l2))
