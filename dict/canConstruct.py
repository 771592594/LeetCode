class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        char_dict = {}
        for c in ransomNote:
            if c in char_dict:
                char_dict[c] += 1
            else:
                char_dict[c] = 1
        for c in magazine:
            if c in char_dict and char_dict[c]:
                char_dict[c] -= 1
        return not any(char_dict.values())


if __name__ == '__main__':
    print(Solution().canConstruct("aa", "aab"))
