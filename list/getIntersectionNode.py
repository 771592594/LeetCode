from common.ListNode import *


# 面试题 02.07. 链表相交
class Solution:
    """
    1. Set  不解释

    2. 双指针
    先求出两条链表的长度，以及它们的长度差d
    让长链表先走d步，让两条链表长度一致，然后两条链表同步走
    链表遍历的同时，判断是否出现相同节点
    """

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        getLen = lambda node: 1 + getLen(node.next) if node else 0
        a_length, b_length = getLen(headA), getLen(headB)
        if a_length > b_length:
            p1, p2, diff = headA, headB, a_length - b_length
        else:
            p1, p2, diff = headB, headA, b_length - a_length
        while diff:
            if p1 == p2:
                return p1
            else:
                p1 = p1.next
                diff -= 1
        while p1:
            if p1 == p2:
                return p1
            p1, p2 = p1.next, p2.next
        return None


if __name__ == '__main__':
    com = create_list_node([4])
    l1 = create_list_node([0, 9, 1])
    l2 = create_list_node([3, 2])
    lastNode(l1).next, lastNode(l2).next = com, com
    print(Solution().getIntersectionNode(l1, l2))
