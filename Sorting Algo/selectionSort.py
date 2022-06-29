def selectionSort(list):
    print("Unsorted list:", list)
    for i in range(0, len(list)):
        min_value_index = i
        for j in range (i+1, len(list)):
            if (list[j] < list[min_value_index]):
                min_value_index = j
        if min_value_index != i:
            list[min_value_index], list[i] = list[i], list[min_value_index]

    print("Sorted List:", list)

selectionSort([10, 9, 7, 3, 2, 1, 4, 5, 10])

