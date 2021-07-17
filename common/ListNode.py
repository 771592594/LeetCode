class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def create_list_node(arr: list):
    if len(arr) == 0:
        return None
    head = ListNode(0)
    temp = head
    for i in arr:
        temp.next = ListNode(i)
        temp = temp.next
    return head.next


def show(node: ListNode):
    s = "["
    cnt = 0
    while node:
        s += str(node.val) if cnt == 0 else ", " + str(node.val)
        node = node.next
        cnt += 1
    s += "]"
    print(s)
