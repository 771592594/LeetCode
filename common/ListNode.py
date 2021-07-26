class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return str(self.val)


def create_list_node(arr: list) -> ListNode:
    if len(arr) < 100:
        return ListNode(arr[0], create_list_node(arr[1:])) if arr else None
    else:
        dummy = ListNode(0)
        tail = dummy
        for i in range(len(arr)):
            node = ListNode(arr[i])
            tail.next = node
            tail = node
        return dummy.next


def traverse(node: ListNode):
    while node:
        print(node.val, end=" ")
        node = node.next
    print()


def remove(head: ListNode, val: int) -> ListNode:
    cur, dummy = head, ListNode(0)
    last = dummy
    while cur:
        if cur.val != val:
            last.next = cur
            last = last.next
        cur = cur.next
    return dummy.next


def deleteNode(node: ListNode):
    node.val = node.next.val
    node.next = node.next.next


def copy(head: ListNode):
    return ListNode(head.val, head.next) if head else None


def lastNode(head: ListNode):
    return head if not head.next else lastNode(head.next)


if __name__ == '__main__':
    node2 = ListNode(2)
    node1 = ListNode(1, node2)
    node = ListNode(0, node1)
    deleteNode(node1)
    traverse(node)
