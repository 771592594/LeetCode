# 901. 股票价格跨度
class StockSpanner:

    def __init__(self):
        self.asc_stack = []

    def next(self, price: int) -> int:
        day = 1
        while self.asc_stack and price >= self.asc_stack[-1][0]:
            day += self.asc_stack.pop()[1]
        self.asc_stack.append((price, day))
        return day


if __name__ == '__main__':
    s = StockSpanner()
    for num in [100, 80, 60, 70, 60, 75, 85]:
        print(s.next(num), end=", ")
