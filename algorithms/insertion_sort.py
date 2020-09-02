from algorithms.sorting_algorithm import SortingAlgorithm

class InsertionSort(SortingAlgorithm):
    def sort(self, arr: list) -> list:
        for i in range(1, len(arr)):
            el = arr[i]
            j = i - 1
            while (j >= 0 and arr[j] > el):
                arr[j + 1] = arr[j]
                j -= 1
        return arr