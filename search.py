def search_arr():
    arr = [2, 6,9]
    target = 9

    low = 0
    high = len(arr) - 1
    found = False

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            print("Found at index", mid)
            found = True
            break

        elif target > arr[mid]:
            low = mid + 1
        else:
            high = mid - 1

    if found == False:
        print("Element not found")

search_arr()