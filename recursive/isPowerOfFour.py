class Solution:
    def rec(self, n: int) -> bool:
        if n == 1:
            return True
        if n % 4:
            return False
        return self.rec(n // 4)

    def isPowerOfFour(self, n: int) -> bool:
        if n == 0:
            return False
        return self.rec(n)


if __name__ == '__main__':
    print(Solution().isPowerOfFour(16))