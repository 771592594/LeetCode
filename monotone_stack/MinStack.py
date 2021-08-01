class MinStack:

    def __init__(self):
        self.stack = []
        # 维护一个单调递增的栈
        self.asc_stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        # 如果元素比单调栈的栈顶元素要小，则压入单调栈
        if not self.asc_stack or x <= self.asc_stack[-1]:
            self.asc_stack.append(x)

    def pop(self) -> None:
        # 如果弹出元素与单调栈的栈顶相同，则弹出单调栈的栈顶
        if self.stack.pop() == self.asc_stack[-1]:
            self.asc_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def min(self) -> int:
        return self.asc_stack[-1]


if __name__ == '__main__':
    o = MinStack()
    o.push(-2)
    o.push(0)
    o.push(-3)
    print(o.min())
    o.pop()
    o.pop()
    print(o.min())