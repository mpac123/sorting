from algorithms.sorting_algorithm import SortingAlgorithm

class SelectionSort(SortingAlgorithm):
    def sort(self, arr: list) -> list:
        for i, el in enumerate(arr):
            curr_min_pos = i
            for j in range(i, len(arr)):
                if arr[j] < arr[curr_min_pos]:
                    curr_min_pos = j
            if i != curr_min_pos:
                arr[i] = arr[curr_min_pos]
                arr[curr_min_pos] = el
        return arr