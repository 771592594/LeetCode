from typing import List


class Solution:
    def rec(self, nums: List[int], used: List[int],
            cur: List[int], ret: List[List[int]]) -> List[List[int]]:
        if all(used):
            ret.append(list(cur))
            return ret
        for i in range(len(nums)):
            if used[i]:
                continue
            used[i] = 1
            cur.append(nums[i])
            self.rec(nums, used, cur, ret)
            cur.pop()
            used[i] = 0
        return ret

    def permute(self, nums: List[int]) -> List[List[int]]:
        return self.rec(nums, [0 for _ in range(len(nums))], [], [])


if __name__ == '__main__':
    print(Solution().permute([1, 2, 3]))
