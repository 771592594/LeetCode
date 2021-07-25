from typing import List


class Solution:
    def rec(self, nums: List[int], used: List[int], cur: List[int], ret: List[List[int]]) -> List[List[int]]:
        if all(used):
            ret.append(list(cur))
            return ret
        for i in range(len(nums)):
            # not used[i - 1] 剪枝效率比 used[i - 1] 更高
            if used[i] or (i > 0 and nums[i] == nums[i - 1] and not used[i - 1]):
                continue
            used[i] = 1
            cur.append(nums[i])
            self.rec(nums, used, cur, ret)
            used[i] = 0
            cur.pop()
        return ret

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        return self.rec(nums, [0 for _ in range(len(nums))], [], [])


if __name__ == '__main__':
    print(Solution().permuteUnique([1, 1, 2]))
