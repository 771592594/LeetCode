class Solution:
    def rec(self, n: int):
        if n == 1:
            return True
        if n % 3:
            return False
        return self.rec(n // 3)

    def isPowerOfThree(self, n: int) -> bool:
        if n == 0:
            return False
        return self.rec(n)


if __name__ == '__main__':
    print(Solution().isPowerOfThree(15))
