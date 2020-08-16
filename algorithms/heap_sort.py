from algorithms.sorting_algorithm import SortingAlgorithm

class HeapSort(SortingAlgorithm):

    class Heap:
        def __init__(self, arr: list, length: int):
            self.arr = arr
            self.length = length

    def sort(self, arr: list) -> list:
        heap = self.Heap(arr, len(arr))
        self.build_max_heap(heap)
        for i in range(heap.length - 1, 0, -1):
            tmp = heap.arr[0]
            heap.arr[0] = heap.arr[i]
            heap.arr[i] = tmp
            heap.length -= 1
            self.max_heapify(heap, 0)
        return heap.arr

    def build_max_heap(self, heap: Heap) -> None:
        # create a heap out of a given list
        for i in range (int(heap.length / 2), -1, -1):
            self.max_heapify(heap, i)

    def max_heapify(self, heap: Heap, index: int) -> None:
        max_index = index
        left_index = self.left_child(index); right_index = self.right_child(index)
        if left_index < heap.length and heap.arr[left_index] > heap.arr[max_index]:
            max_index = left_index
        if right_index < heap.length and heap.arr[right_index] > heap.arr[max_index]:
            max_index = right_index
        if max_index != index:
            tmp = heap.arr[index]
            heap.arr[index] = heap.arr[max_index]
            heap.arr[max_index] = tmp
            self.max_heapify(heap, max_index)
        
    def left_child(self, index: int) -> int:
        return 2 * index

    def right_child(self, index: int) -> int:
        return 2 * index + 1

