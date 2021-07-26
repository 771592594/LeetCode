from common.ListNode import *


# 83. 删除排序链表中的重复元素
class Solution:
    """
    双指针
    将原链表中不重复的元素转移到新链表中
    在原链表上添加一个虚拟头节点
    从虚拟头节点开始遍历，每次查找下一个与当前节点值不同的节点 next_diff
    如果 next_diff 是尾节点，则直接插入新链表中
    如果 next_diff 是中间节点且后继与它不同，则插入新链表中
    """

    def next_diff_node(self, node: ListNode, target: ListNode) -> ListNode:
        if not node:
            return node
        return node if node.val != target.val else self.next_diff_node(node.next, target)

    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        dummy, ret = ListNode(-999, head), ListNode(0)
        node, tail = dummy, ret
        while node:
            # 找出下一个不同的节点
            next_diff = self.next_diff_node(node, node)
            # 如果是中间节点，要求它与后继节点的值不相同
            if next_diff and next_diff.next and next_diff.val != next_diff.next.val:
                tail.next = next_diff
                tail = next_diff
            # 如果是尾节点，必然不存在相同的节点
            if next_diff and not next_diff.next:
                tail.next = next_diff
                tail = next_diff
            node = next_diff
        tail.next = None
        return ret.next


if __name__ == '__main__':
    l1 = Solution().deleteDuplicates(create_list_node([1, 2, 3, 3, 4, 4, 5]))
    traverse(l1)
