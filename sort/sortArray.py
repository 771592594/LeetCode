from typing import List


class Solution:
    """
    归并排序
    """
    def mergeSort(self, nums: List[int], left: int, right: int):
        def merge(left: int, right: int, right_bound: int):
            if nums[right] >= nums[right - 1]:
                return
            i, j, sorted_arr = left, right, []
            # 归并子数组
            while i < right and j <= right_bound:
                if nums[i] < nums[j]:
                    sorted_arr.append(nums[i])
                    i += 1
                else:
                    sorted_arr.append(nums[j])
                    j += 1
            for idx in range(i, right):
                sorted_arr.append(nums[idx])
            for idx in range(j, right_bound + 1):
                sorted_arr.append(nums[idx])
            # 拷贝回原数组
            for idx, value in enumerate(sorted_arr):
                nums[left + idx] = value

        if left >= right:
            return
        mid = (left + right) >> 1
        self.mergeSort(nums, left, mid)
        self.mergeSort(nums, mid + 1, right)
        merge(left, mid + 1, right)

    """
    堆排序
    """
    def heapSort(self, nums: List[int]):
        self.buildHeap(nums)
        for i in range(len(nums) - 1, -1, -1):
            nums[0], nums[i] = nums[i], nums[0]
            self.maxHeaify(nums, 0, i)

    def buildHeap(self, nums: List[int]):
        for i in range(len(nums) - 1, -1, -1):
            self.maxHeaify(nums, i, len(nums))

    def maxHeaify(self, heap: list, root: int, size: int):
        largest, left, right = root, root * 2 + 1, root * 2 + 2
        if left < size and heap[largest] < heap[left]:
            largest = left
        if right < size and heap[largest] < heap[right]:
            largest = right
        if largest != root:
            heap[root], heap[largest] = heap[largest], heap[root]
            self.maxHeaify(heap, largest, size)

    def sortArray(self, nums: List[int]) -> List[int]:
        # self.mergeSort(nums, 0, len(nums) - 1)
        self.heapSort(nums)
        return nums


if __name__ == '__main__':
    arr = [2, 4, 1, 3, 0]
    print(Solution().sortArray(arr))
