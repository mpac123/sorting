import pytest
from algorithms.sorting_algorithm import SortingAlgorithm
import algorithms

test_cases = [  
            ([],[]), 
            ([1],[1]),
            ([1,2],[1,2]),
            ([2,1],[1,2]),
            ([1,2,3],[1,2,3]), 
            ([0,0,0],[0,0,0]), 
            ([3,2,1],[1,2,3]), 
            ([5,3,7,9,1],[1,3,5,7,9]),
            ([1,2,3,-10,4,5],[-10,1,2,3,4,5]),
            ([51,127,13,5,1002],[5,13,51,127,1002])
            ]

@pytest.mark.parametrize("algorithm", SortingAlgorithm.__subclasses__())
@pytest.mark.parametrize("array,sorted_array", test_cases)
def test(array, sorted_array, algorithm: SortingAlgorithm):
    assert algorithm().sort(array) == sorted_array

