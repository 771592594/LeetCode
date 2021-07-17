# 50. Pow(x, n)
class Solution:
    def quick_mul(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n & 1:
            return x * self.quick_mul(x, n - 1)
        else:
            temp = self.quick_mul(x, n // 2)
            return temp * temp

    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n
        return self.quick_mul(x, n)


if __name__ == '__main__':
    print(Solution().myPow(2, 10))
