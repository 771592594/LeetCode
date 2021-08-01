from typing import List


# 1475. 商品折扣后的最终价格
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        # 使用列表构造一个单调递减的栈，列表最后一个元素为栈顶元素
        desc_stack = []
        ans = [price for price in prices]
        for idx, price in enumerate(prices):
            # 找到栈顶元素后面第一个价格比它低的元素，计算折扣后的最终价格
            while desc_stack and price <= desc_stack[-1][1]:
                top = desc_stack.pop()
                ans[top[0]] = top[1] - price
            desc_stack.append([idx, price])
        return ans


if __name__ == '__main__':
    print(Solution().finalPrices([8, 4, 6, 2, 3]))
