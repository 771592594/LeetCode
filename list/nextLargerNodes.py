from typing import List

from common.ListNode import *


# 1019. 链表中的下一个更大节点
class Solution:

    """
    单调栈
    """

    def nextLargerNodes(self, head: ListNode) -> List[int]:
        # 单调栈从左到右递减
        idx, stack, next_larger = 0, [], []
        while head:
            while stack and head.val > stack[-1][1]:
                entry = stack.pop()
                next_larger[entry[0]] = head.val
            stack.append([idx, head.val])
            next_larger.append(0)
            head = head.next
            idx += 1
        return next_larger

    """
    二重循环（超时）
    维护两个数组 nums 和 larger
    """

    def nextLargerNodes1(self, head: ListNode) -> List[int]:
        node = head
        idx, nums, larger, not_find_larger = -1, [], [], []
        while node:
            idx += 1
            nums.append(node.val)
            for i in list(not_find_larger):
                if nums[i] < node.val:
                    larger[i] = node.val
                    not_find_larger.remove(i)
            larger.append(0)
            not_find_larger.append(idx)
            node = node.next
        return larger


if __name__ == '__main__':
    arr = [2, 7, 4, 3, 5]
    print(Solution().nextLargerNodes(create_list_node(arr)))
