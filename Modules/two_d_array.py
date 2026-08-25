import numpy as np
numbers = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print(numbers)
print(numbers[0, 0])
print(numbers[0, 1])
print(numbers[1, 0])
print(numbers[1, 1])
print(numbers[0])
print(numbers[1])
print(numbers[:,0])
print(numbers[:,1])
print(numbers[:,2])

numbers = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])
print(numbers[1, 1])
print(numbers[2, 2])
print(numbers[0 , :])
print(numbers[:, 2])
print(numbers[:, 0])
print(numbers[:, 1])
print(numbers.max())
print(numbers.sum())