from typing import List


# 剑指 Offer 40. 最小的k个数
class Solution:
    """
    堆排序
    """
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        def __up(node):
            parent = (node - 1) >> 1
            if parent >= 0 and max_heap[node] > max_heap[parent]:
                max_heap[node], max_heap[parent] = max_heap[parent], max_heap[node]
                __up(parent)

        def __down(root):
            largest, left, right = root, root * 2 + 1, root * 2 + 2
            if left < len(max_heap) and max_heap[left] > max_heap[largest]:
                largest = left
            if right < len(max_heap) and max_heap[right] > max_heap[largest]:
                largest = right
            if root != largest:
                max_heap[root], max_heap[largest] = max_heap[largest], max_heap[root]
                __down(largest)

        if not k:
            return []
        # 建容量为K的大根堆，将原数组插入到堆中
        max_heap = [] * k
        for i in range(len(arr)):
            if len(max_heap) < k:
                max_heap.append(arr[i])
                __up(i)
            elif arr[i] < max_heap[0]:
                max_heap[0] = arr[i]
                __down(0)
        return max_heap


if __name__ == '__main__':
    # print(Solution().getLeastNumbers([2, 3, 1, 4, 5], 2))
    print(Solution().getLeastNumbers([0, 0, 1, 2, 4, 2, 2, 3, 1, 4], 8))
