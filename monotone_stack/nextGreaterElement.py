from typing import List


# 496. 下一个更大元素 I
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = [-1 for _ in nums1]
        # 为nums1的元素建立{value: idx}的字典
        target_map = {value: idx for idx, value, in enumerate(nums1)}
        # 构建一个单调递增栈，以列表的最后一个元素作为栈顶
        asc_stack = []
        for num in nums2:
            # 如果当前元素比栈顶元素大，则说明找到了栈顶元素在nums中的下一个更大元素
            while asc_stack and num > asc_stack[-1][1]:
                idx = asc_stack.pop()[0]
                ans[idx] = num
            # 如果当前元素是字典的key，则该元素需要找下个更大值，将其值和在nums中的索引压入单调栈
            if num in target_map:
                # 单调栈为了保持有序性，需要将值比入栈元素大的项出栈；当前项入栈后，再压回去
                less_values = []
                while asc_stack and num > asc_stack[-1][1]:
                    less_values.append(asc_stack.pop())
                asc_stack.append([target_map[num], num])
                while less_values:
                    asc_stack.append(less_values.pop())
        return ans


if __name__ == '__main__':
    print(Solution().nextGreaterElement(nums1=[2, 4], nums2=[1, 2, 3, 4]))
