from algorithms.sorting_algorithm import SortingAlgorithm

class QuickSort(SortingAlgorithm):
    
    def sort(self, arr: list) -> list:
        return self.quick_sort(arr, 0, len(arr))

    def quick_sort(self, arr: list, left: int, right: int) -> list:
        
        # finish recursion if array is empty or with one element
        if right - left <= 1:
            return arr

        pivot_curr_pos = self.choose_pivot_pos(arr, left, right)
        pivot_correct_pos = self.quick_sort_single_pass(arr, left, right, pivot_curr_pos)

        self.quick_sort(arr, left, pivot_correct_pos)
        self.quick_sort(arr, pivot_correct_pos + 1, right)
        return arr

    def quick_sort_single_pass(self, arr: list, left: int, right: int, pivot_pos: int) -> int:

        # move pivot to the rightmost position
        temp = arr[right - 1]
        arr[right - 1] = arr[pivot_pos]
        arr[pivot_pos] = temp

        # swap till pivot's position found
        greater_from_left_pos = left
        smaller_from_right_pos = right - 1
        while greater_from_left_pos < smaller_from_right_pos:
            # find first from left value greater than pivot
            while greater_from_left_pos < right - 1 and arr[greater_from_left_pos] <= arr[right - 1]:
                greater_from_left_pos += 1
            # find first from right value smaller than pivot
            while smaller_from_right_pos >= left and arr[smaller_from_right_pos] >= arr[right - 1]:
                smaller_from_right_pos -= 1
            # swap values
            if greater_from_left_pos < smaller_from_right_pos:
                temp = arr[greater_from_left_pos]
                arr[greater_from_left_pos] = arr[smaller_from_right_pos]
                arr[smaller_from_right_pos] = temp
        # move pivot to its correct position
        if greater_from_left_pos < right - 1:
            temp = arr[right - 1]
            arr[right - 1] = arr[greater_from_left_pos]
            arr[greater_from_left_pos] = temp

        return greater_from_left_pos


    def choose_pivot_pos(self, arr: list, left: int, right: int) -> int:
        # median of 3
        if left == right:
            return left
        medium = (right + left) // 2
        if arr[left] <= arr[medium]:
            if arr[right - 1] <= arr[left]:
                return left
            elif arr[right - 1] <= arr[medium]:
                return right - 1
            else:
                return medium
        else:
            if arr[right - 1] <= arr[medium]:
                return medium
            elif arr[right - 1] <= arr[left]:
                return right - 1
            else:
                return left