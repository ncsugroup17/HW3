"""
Import for random array generation
"""
import rand

def merge_sort(arr_param):
    """
    The merge sort algorithm
    """
    # Base case had to be fixed to <= 1
    if len(arr_param) <= 1:
        return arr_param

    half = len(arr_param)//2

    return recombine(merge_sort(arr_param[:half]), merge_sort(arr_param[half:]))

def recombine(left_arr, right_arr):
    """
    The recombine function
    """
    left_index = 0
    right_index = 0
    merge_arr = [None] * (len(left_arr) + len(right_arr))
    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] < right_arr[right_index]:
            # The right index was being updated here, switched to left index
            merge_arr[left_index + right_index] = left_arr[left_index]
            left_index += 1
        else:
            # The left index was being updated here, switched to right index
            merge_arr[left_index + right_index] = right_arr[right_index]
            right_index += 1

    # The size of the merge array was being calculated incorrectly
    size = left_index + right_index
    for i in range(right_index, len(right_arr)):
        merge_arr[size] = right_arr[i]
        size += 1

    for i in range(left_index, len(left_arr)):
        merge_arr[size] = left_arr[i]
        size += 1

    return merge_arr

# Create a new sorting algorithm with issues
def is_duplicate(nums):
    """
    My personal isDuplicate function
    """
    seen = set()

    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

arr = rand.random_array([None] * 20)
print(arr)
arr_out = merge_sort(arr)
print(arr_out)

nums1 = [1, 2, 3, 4, 5]
nums2 = [1, 2, 3, 4, 1]

print(is_duplicate(nums1))  # Output: False
print(is_duplicate(nums2))  # Output: True
