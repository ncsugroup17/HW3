import rand

def mergeSort(arr):
    # Base case had to be fixed to <= 1
    if (len(arr) <= 1):
        return arr

    half = len(arr)//2

    return recombine(mergeSort(arr[:half]), mergeSort(arr[half:]))

def recombine(leftArr, rightArr):
    leftIndex = 0
    rightIndex = 0
    mergeArr = [None] * (len(leftArr) + len(rightArr))
    while leftIndex < len(leftArr) and rightIndex < len(rightArr):
        if leftArr[leftIndex] < rightArr[rightIndex]:
            # The right index was being updated here, switched to left index
            mergeArr[leftIndex + rightIndex] = leftArr[leftIndex]
            leftIndex += 1
        else:
            # The left index was being updated here, switched to right index
            mergeArr[leftIndex + rightIndex] = rightArr[rightIndex]
            rightIndex += 1

    # The size of the merge array was being calculated incorrectly
    size = leftIndex + rightIndex
    for i in range(rightIndex, len(rightArr)):
        mergeArr[size] = rightArr[i]
        size += 1
    
    for i in range(leftIndex, len(leftArr)):
        mergeArr[size] = leftArr[i]
        size += 1
    
    return mergeArr

def is_happy(n):
    """
    Determines if a number is a happy number.
    :type n: int
    :rtype: bool
    """
    
    def find_sum_of_digit(num):
        """
        Helper function to calculate the sum of squares of the digits of a number.
        :type num: int
        :rtype: int
        """
        string_num = str(num)
        result_sum = 0
        for digit in string_num:
            result_sum += int(digit) ** 2
        return result_sum

    seen_numbers = {}
    while True:
        if n in seen_numbers:
            return False
        seen_numbers[n] = n
        if n == 1:
            return True
        n = find_sum_of_digit(n)


# Example usage
HAPPY_NUMBER = 19
IS_HAPPY_RESULT = is_happy(HAPPY_NUMBER)
print(f"Is {HAPPY_NUMBER} a happy number? {IS_HAPPY_RESULT}")

arr = rand.random_array([None] * 20)
print(arr)
arr_out = mergeSort(arr)

print(arr_out)


