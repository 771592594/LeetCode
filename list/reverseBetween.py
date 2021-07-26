from common.ListNode import *


# 92. 反转链表 II
class Solution:
    """
    分割 反转 合并
    """
    # todo 未完待续
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        cnt, node = 0, head
        while node:
            cnt += 1
            if left == cnt - 1:
                left_node = node
            elif right == cnt:
                right_node = node
                break

