#Sort an array using Bubble Sort.
def bubble_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


arr = [5, 3, 1, 4, 2]

print("Before sorting:", arr)
print("After sorting:", bubble_sort(arr))

#sort in descending order
def bubble_sort_descending(arr):
    n = len(arr)

    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


arr = [55,23,13,46,4]

print(bubble_sort_descending(arr))

#Count total swaps.
def bubble_sort_swaps(arr):
    n=len(arr)
    swaps=0

    for i in range(n - 1):
        for j in range(n - 1 -i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1]=arr[j+1],arr[j]
                swaps += 1

    print(arr)
    print(swaps)

arr =[3,2,7,1,9]
bubble_sort_swaps(arr)

#Count total comparisons.
def bubble_sort_comparisons(arr):
    n=len(arr)
    comparisons=0

    for i in range(n - 1):
        for j in range(n - 1 -i):
            comparisons +=1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1]=arr[j+1],arr[j]
    
    print(arr)
    print(comparisons)

arr=[3,6,2,5,4]
bubble_sort_comparisons(arr)

#Detect whether the array is already sorted.
def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False

    return True


arr = [6,2,1,8,3,7]

if is_sorted(arr):
    print("Array is already sorted")
else:
    print("Array is not sorted")

#Print the array after every pass.
def bubble_sort_print_passes(arr):
    n = len(arr)

    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

        print("After pass", i + 1, ":", arr)

    return arr


arr = [5, 3, 4, 1, 2]
bubble_sort_print_passes(arr)

#Stop early if already sorted.
def optimized_bubble_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        swapped = False

        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if swapped == False:
            break

    return arr

arr = [4,7,5,9,1,3]
print(optimized_bubble_sort(arr))
