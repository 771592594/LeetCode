from typing import List


# 739. 每日温度
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # 使用列表构造一个单调递增的栈，列表最后一个元素为栈顶元素
        asc_stack = []
        ans = [0 for _ in temperatures]
        for idx, val in enumerate(temperatures):
            # 如果当前温度比栈顶的温度高，则出栈计算它们之间天数
            while asc_stack and val > asc_stack[-1][1]:
                last_idx = asc_stack.pop()[0]
                ans[last_idx] = idx - last_idx
            asc_stack.append([idx, val])
        return ans


if __name__ == '__main__':
    print(Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
