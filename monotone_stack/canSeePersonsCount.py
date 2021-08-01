from typing import List


# 1944. 队列中可以看到的人数
class Solution:
    """
    一个人只能看到
    他与右边第一个比他高的人之间的人
    """
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        # 维护一个单调递增的栈
        asc_stack = []
        ans = [0] * len(heights)
        for i in range(len(heights) - 1, -1, -1):
            # 将比当前值小的栈顶元素出栈
            while asc_stack and heights[i] > asc_stack[-1]:
                asc_stack.pop()
                ans[i] += 1
            # 如果栈非空，说明有比当前值更大的元素存在，这个元素也是可见的
            if asc_stack:
                ans[i] += 1
            asc_stack.append(heights[i])
        return ans


if __name__ == '__main__':
    print(Solution().canSeePersonsCount([5, 1, 2, 3, 10]))
