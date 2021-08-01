# 面试题 03.05. 栈排序
class SortedStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        greater = []
        while self.stack and val > self.stack[-1]:
            greater.append(self.stack.pop())
        self.stack.append(val)
        if greater:
            self.stack.append(greater[::-1])

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()

    def peek(self) -> int:
        return self.stack[-1] if self.stack else -1

    def isEmpty(self) -> bool:
        return len(self.stack) == 0
