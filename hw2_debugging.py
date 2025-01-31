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

arr = rand.random_array([None] * 20)
print(arr)
arr_out = mergeSort(arr)

print(arr_out)


