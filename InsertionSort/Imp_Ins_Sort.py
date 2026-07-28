#Implement Insertion Sort.
def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


arr = [5, 3, 1, 4, 2]
print(insertion_sort(arr))

#Sort descending.
def sort_descending(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr

arr = [5, 3, 1, 4, 2]
print(sort_descending(arr))

#Count shifts.
def sort_shift(arr):
    n = len(arr)
    shift =0

    for i in range(1, n):
        key = arr[i]
        j = i - 1
        shift +=1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key
    
    print("No of shift:",shift)

    return arr

arr = [5, 3, 1, 4, 2]
print(sort_shift(arr))

#Print every insertion.
def insertion_sort_print_every_insertion(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        print("Pass", i)
        print("Key selected:", key)

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

        print("Array after insertion:", arr)
        print()

    return arr


arr = [5, 3, 1, 4, 2]
print("Before sorting:", arr)
insertion_sort_print_every_insertion(arr)
print("After sorting:", arr)

# #Count comparisons
def sort_shift(arr):
    n = len(arr)
    shift =0

    for i in range(1, n):
        key = arr[i]
        j = i - 1
        shift +=1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key
    
    print("No of shift:",shift)

    return arr

arr = [5, 3, 1, 4, 2]
print(sort_shift(arr))

Count comparisons
Count comparisons in Insertion Sort

def sort_comparisons(arr):
    n = len(arr)
    comparisons = 0

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0:
            comparisons += 1

            if arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            else:
                break

        arr[j + 1] = key
        
    print("Total comparisons:", comparisons)
    return arr


arr = [5, 3, 1, 4, 2]
print(sort_comparisons(arr))