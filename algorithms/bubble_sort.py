from algorithms.sorting_algorithm import SortingAlgorithm

class BubbleSort(SortingAlgorithm):

    def sort(self, arr: list) -> list:
        is_sorted = False
        while(not is_sorted):
            is_sorted = True
            for i in range(0, len(arr)-1):
                if arr[i] > arr[i+1]:
                    is_sorted = False
                    temp = arr[i]
                    arr[i] = arr[i+1]
                    arr[i+1] = temp
        return arr
