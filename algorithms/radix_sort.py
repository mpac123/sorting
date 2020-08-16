from algorithms.sorting_algorithm import SortingAlgorithm
import math 

class RadixSort(SortingAlgorithm):

    def sort(self, arr: list) -> list:
        if (len(arr) == 0):
            return arr
        max_nr_digits = max([len(str(item)) for item in arr])
        for digit_nr in range(1, max_nr_digits + 1):
            self.sort_by_key(arr, digit_nr)
        return arr

    def sort_by_key(self, arr: list, key_digit: int) -> list:
        list_per_digit = [[] for _ in range(0,10)]
        for el in arr:
            list_per_digit[self.take_nth_least_significant_digit(el, key_digit)].append(el)
        return [item for sublist in list_per_digit for item in sublist]

    def take_nth_least_significant_digit(self, number: int, n: int) -> int:
        return (number % pow(10, n)) // pow(10,n-1)

sort = RadixSort()
res = sort.sort_by_key([5,4,3,7,10], 3)