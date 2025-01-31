"""
Unit tests for the mergeSort function from hw2_debugging.py
"""
from hw2_debugging import mergeSort

def test_unsorted_array_with_unique_elements():
    """
    Test mergeSort with an unsorted array containing unique elements.
    """
    arr = [38, 27, 43, 3, 9, 82, 10]
    expected = [3, 9, 10, 27, 38, 43, 82]
    assert mergeSort(arr) == expected

def test_array_with_duplicates():
    """
    Test mergeSort with an array containing duplicate elements.
    """
    arr = [5, 1, 4, 2, 8, 5, 3]
    expected = [1, 2, 3, 4, 5, 5, 8]
    assert mergeSort(arr) == expected

def test_already_sorted_array():
    """
    Test mergeSort with an already sorted array.
    """
    arr = [1, 2, 3, 4, 5]
    expected = [1, 2, 3, 4, 5]
    assert mergeSort(arr) == expected

def test_empty_array():
    """
    Test mergeSort with an empty array.
    """
    arr = []
    expected = []
    assert mergeSort(arr) == expected

def test_one_item_in_list():
    """
    Test mergeSort with an array containing a single element.
    """
    arr = [100]
    expected = [100]
    assert mergeSort(arr) == expected
