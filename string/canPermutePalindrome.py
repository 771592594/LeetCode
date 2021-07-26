class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        """
        字符可以组成回文字符串的条件:
        1.每种字符都出现两次
        2.一种字符出现一次，其余都出现两次
        """
        c_set = set()
        for c in s:
            if c in c_set:
                c_set.remove(c)
            else:
                c_set.add(c)
        return len(c_set) <= 1


if __name__ == '__main__':
    s = "code"
    print(Solution().canPermutePalindrome(s))