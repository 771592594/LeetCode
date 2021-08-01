from typing import List


# 40. 组合总和 II
class Solution:
    """
    去重的关键点：在同一层的递归中，相等的元素只取第一个
    """
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrace(begin: int, path, residue: int):
            if residue == 0:
                ans.append(path[:])
                return
            for idx in range(begin, size):
                # 因为数组是升序的，如果当前元素比残余值要大，则回溯
                if residue < candidates[idx]:
                    break
                # 在同一层递归中，相等的元素只取第一个
                if idx > begin and candidates[idx] == candidates[idx - 1]:
                    continue
                path.append(candidates[idx])
                backtrace(idx + 1, path, residue - candidates[idx])
                path.pop()

        ans = []
        size = len(candidates)
        candidates.sort()
        backtrace(0, [], target)
        return ans


if __name__ == '__main__':
    # print(Solution().combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
    print(Solution().combinationSum2([1, 2, 2, 2, 5], 5))
    arr = [14, 6, 25, 9, 30, 20, 33, 34, 28, 30, 16, 12, 31, 9, 9, 12, 34, 16, 25, 32, 8, 7, 30, 12, 33, 20, 21, 29, 24,
           17, 27, 34, 11, 17, 30, 6, 32, 21, 27, 17, 16, 8, 24, 12, 12, 28, 11, 33, 10, 32, 22, 13, 34, 18, 12]
    # print(Solution().combinationSum2(arr, 27))
