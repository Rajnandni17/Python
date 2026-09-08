#Implement Selection Sort.
def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


arr = [5, 3, 1, 4, 2]

print("Before sorting:", arr)
print("After sorting:", selection_sort(arr))

#Sort descending.
def selection_sort_descending(arr):
    n = len(arr)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] > arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


arr = [5, 3, 1, 4, 2]

print("Before sorting:", arr)
print("After sorting:", selection_sort_descending(arr))

#Count swaps.
def selection_sort_swaps(arr):
    n = len(arr)
    swaps =0

    for i in range(n):
        min_index = i
    

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        if min_index !=i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            swaps +=1


    print(arr)
    print(swaps)

    return arr


arr = [5, 3, 1, 4, 2]
selection_sort_swaps(arr)

#Count total comparisons. 
def selection_sort_comparisons(arr):
    n = len(arr)
    comparisons =0

    for i in range(n):
        min_index = i
    

        for j in range(i + 1, n):
            comparisons +=1

            if arr[j] < arr[min_index]:
                min_index = j

        if min_index !=i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            


    print(arr)
    print(comparisons)

    return arr


arr = [5, 3, 1, 4, 2]
selection_sort_comparisons(arr)

#Print minimum element selected every pass.
def selection_sort_print_min(arr):
    n = len(arr)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        print("Pass", i + 1)
        print("Minimum selected:", arr[min_index])
        print("Minimum index:", min_index)

        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]

        print("Array after pass:", arr)

    return arr

arr = [5, 3, 1, 4, 2]
selection_sort_print_min(arr)

#Print array after every pass.
def selection_sort_print_pass(arr):
    n = len(arr)

    for i in range(n - 1):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]

        print("Pass", i + 1, ":", arr)

    return arr


arr = [5, 3, 1, 4, 2]

print("Before sorting:", arr)
selection_sort_print_pass(arr)
print("After sorting:", arr)

