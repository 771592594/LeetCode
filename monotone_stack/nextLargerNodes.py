from typing import List

from common.ListNode import *


# 1019. 链表中的下一个更大节点
class Solution:
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


if __name__ == '__main__':
    arr = [2, 7, 4, 3, 5]
    print(Solution().nextLargerNodes(create_list_node(arr)))
