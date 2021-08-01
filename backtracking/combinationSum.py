from typing import List


# 39. 组合总和
class Solution:
    """
    结果集去重的关键是：每次递归时，都从当前选择元素及其右边开始访问，左侧的元素不再访问
    """
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(begin: int, residue: int, path: list):
            if residue == 0:
                return ans.append(path[:])
            for idx in range(begin, size):
                # 因为数组是升序的，如果当前元素小于残余值，则不必继续访问
                if residue < candidates[idx]:
                    break
                path.append(candidates[idx])
                backtrack(idx, residue - candidates[idx], path)
                path.pop()

        ans = []
        # 排序数组，方便剪枝
        candidates.sort()
        size = len(candidates)
        backtrack(0, target, [])
        return ans


if __name__ == '__main__':
    print(Solution().combinationSum([2, 3, 6, 7], 7))
    print(Solution().combinationSum([2, 3, 5], 8))
