from typing import List


# 703. 数据流中的第 K 大元素
class KthLargest:
    """
    堆排序
    构建长度为K的小根堆，根节点是最小的数，也就是最大第K个数
    插入新元素时，如果新元素比根大，则删除根，在根的位置上插入新元素
    最后堆根节点进行冒泡交换元素，保持堆的有效性
    """

    def __init__(self, k: int, nums: List[int]):
        self.rank = k
        self.heap = []
        self.count = 0
        for num in nums:
            self.add(num)
        print(self.heap)

    def add(self, val: int) -> int:
        # 若堆元素小于K，则插入元素再上浮，保持堆的有效性
        if self.count < self.rank:
            self.count += 1
            self.heap.append(val)
            self.__up(self.count - 1)
        # 若新增元素大于根，则替换调根再下沉，保持堆的有效性
        elif val > self.heap[0]:
            self.heap[0] = val
            self.__down(0)
        return self.heap[0]

    # 下沉
    def __down(self, node: int):
        count, heap = self.count, self.heap
        least, left, right = node, node * 2 + 1, node * 2 + 2
        if left < count and heap[least] > heap[left]:
            least = left
        if right < count and heap[least] > heap[right]:
            least = right
        if least != node:
            heap[node], heap[least] = heap[least], heap[node]
            self.__down(least)

    # 上浮
    def __up(self, node: int):
        heap = self.heap
        least, parent = node, (node - 1) // 2
        if parent >= 0 and heap[node] < heap[parent]:
            heap[node], heap[parent] = heap[parent], heap[node]
            self.__up(parent)


if __name__ == '__main__':
    # kthLargest = KthLargest(3, [4, 5, 8, 2])
    # arr = [3, 5, 10, 9, 4]
    # print([i for i in map(kthLargest.add, arr)])

    kthLargest = KthLargest(2, [0])
    arr = [-1, 1, -2, -4, 3]
    print([i for i in map(kthLargest.add, arr)])

    # kthLargest = KthLargest(7, [-10, 1, 3, 1, 4, 10, 3, 9, 4, 5, 1])
    # arr = [3, 2, 3, 1, 2, 4, 5, 5, 6, 7, 7, 8, 2, 3, 1, 1, 1, 10, 11, 5, 6, 2, 4, 7, 8, 5, 6]
    # print([i for i in map(kthLargest.add, arr)])
