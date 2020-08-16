from algorithms.sorting_algorithm import SortingAlgorithm

class InsertionSort(SortingAlgorithm):
    def sort(self, arr: list) -> list:
        for i, el in enumerate(arr):
            j = i
            while (j > 0 and arr[j] < arr[j-1]):
                arr[j] = arr[j-1]
                arr[j-1] = el
                j -= 1
        return arr