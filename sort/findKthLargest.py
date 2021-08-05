from typing import List


# 215. 数组中的第K个最大元素
class Solution:
    """
    1. 将原数组转化成大根堆，进行K次pop()操作，得到第K大

    2. 根据截取原数组的前K个元素创建大小为K的小根堆，
    将剩余元素与根比较，比根大则插入堆中，并移除根节点
    这样构造出的最小堆的根元素就是最大第K个元素
    """
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def __down(node, size):
            """
            下沉节点
            :param node: 当前节点的索引
            :param size: 堆的大小
            :return:     None
            """
            largest, left, right = node, node * 2 + 1, node * 2 + 2
            if left < size and nums[largest] < nums[left]:
                largest = left
            if right < size and nums[largest] < nums[right]:
                largest = right
            if node != largest:
                nums[node], nums[largest] = nums[largest], nums[node]
                __down(largest, size)

        # 构造一个大根堆
        max_heap, size = [], len(nums)
        for i in range(size - 1, -1, -1):
            max_heap.append(nums[i])
            __down(i, size)
        # 堆排序K次
        for i in range(k):
            nums[0], nums[size - i - 1] = nums[size - i - 1], nums[0]
            __down(0, size - i - 1)
        return nums[size - k]


if __name__ == '__main__':
    print(Solution().findKthLargest([3, 2, 1, 5, 6, 4], 2))
