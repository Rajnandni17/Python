arr = [10, 20, 30, 40, 50]

target = 40

found = False

for i in range(len(arr)):

    if arr[i] == target:
        print("Found at index", i)
        found = True
        break

if found == False:
    print("Not Found")