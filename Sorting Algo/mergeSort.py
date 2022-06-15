def mergeSort(array):
    if len(array)<=1:
        return array
    midpoint= int(len(array)/2)

    left = mergeSort(array[:midpoint])
    right= mergeSort(array[midpoint:])


    return merge(left, right)

def merge(left, right):
    result = []

    leftPointer= 0
    rightPointer= 0

    while leftPointer< len(left) and rightPointer< len(right):

        if left[leftPointer] < right[rightPointer]:
            result.append(left[leftPointer])
            leftPointer += 1

        else:
            result.append(right[rightPointer])
            rightPointer += 1

    result.extend(left[leftPointer:])
    result.extend(right[rightPointer:])

    return result


print(mergeSort([4,2,5,9,3,5,8,1,7,2,5,3,8,4,2,5,7]))