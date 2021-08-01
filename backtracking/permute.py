from typing import List


# 46. 全排列
class Solution:
    def backtrack(self, nums: List[int], used: List[int],
                  cur: List[int], ret: List[List[int]]) -> List[List[int]]:
        if all(used):
            ret.append(list(cur))
            return ret
        for i in range(len(nums)):
            if used[i]:
                continue
            used[i] = 1
            cur.append(nums[i])
            self.backtrack(nums, used, cur, ret)
            cur.pop()
            used[i] = 0
        return ret

    def permute(self, nums: List[int]) -> List[List[int]]:
        return self.backtrack(nums, [0 for _ in range(len(nums))], [], [])


if __name__ == '__main__':
    print(Solution().permute([1, 2, 3]))
