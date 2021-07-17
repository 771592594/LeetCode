from typing import List

from common.ListNode import *


class Solution:
    def rec(self, node: ListNode, ret: List[int]) -> List[int]:
        if not node:
            return ret
        self.rec(node.next, ret)
        ret.append(node.val)
        return ret

    def reversePrint(self, head: ListNode) -> List[int]:
        return self.rec(head, [])


if __name__ == '__main__':
    print(Solution().reversePrint(create_list_node([1, 2, 3, 4, 5])))
