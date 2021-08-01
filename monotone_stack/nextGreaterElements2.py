from typing import List

# 503. 下一个更大元素 II
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # 构建一个单调递增栈，以列表的最后一个元素作为栈顶
        asc_stack = []
        ans = [-1 for _ in nums]
        # 第一次遍历，找出每个元素在单向数组中的下一个更大元素
        for idx, num in enumerate(nums):
            while asc_stack and num > asc_stack[-1][1]:
                ans[asc_stack.pop()[0]] = num
            asc_stack.append([idx, num])
        # 第二次遍历，找出剩余元素在循环数组中的下一个更大元素
        for idx, num in enumerate(nums):
            while asc_stack and num > asc_stack[-1][1]:
                ans[asc_stack.pop()[0]] = num
        return ans


if __name__ == '__main__':
    print(Solution().nextGreaterElements([1, 2, 1]))
