from algorithms.sorting_algorithm import SortingAlgorithm

class MergeSort(SortingAlgorithm):

    def sort(self, arr: list) -> list:
        self.divide_and_merge(arr, 0, len(arr))
        return arr

    def divide_and_merge(self, arr: list, left: int, right: int):
        
        # finish recursion if array is empty or contains only one element
        if right - left <= 1:
            return

        middle = left + int((right - left) / 2)
        self.divide_and_merge(arr, left, middle)
        self.divide_and_merge(arr, middle, right)
        self.merge(arr, left, middle, right)

    def merge(self, arr: list, left: int, middle: int, right: int):
        i = left; j = middle
        merged = []
        while i < middle or j < right:
            if i == middle:
                merged.append(arr[j])
                j += 1
            elif j == right:
                merged.append(arr[i])
                i += 1
            elif arr[i] <= arr[j]:
                merged.append(arr[i])
                i += 1
            else:
                merged.append(arr[j])
                j += 1
        arr[left:right] = merged