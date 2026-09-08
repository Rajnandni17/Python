import numpy as np

# numbers = np.array([10, 20, 30, 40])

# print(numbers)
# print(numbers.sum())
# print(numbers.mean())
# print(numbers.max())
# print(numbers.min())
# print(numbers * 2)
# print(numbers[0])
# print(numbers[2])
# print(numbers[1:3])
# print(numbers[numbers > 20])

marks = np.array([45, 78, 32, 90, 66, 25])

print(marks[marks > 50])
print(marks[ marks < 40])
print(marks[ marks >= 60])
print(marks.max())
print(marks.min())
print(marks.mean())
print(marks+5)
print(marks * 2)
print(marks[:3])
print(marks[-3:])
print(marks ** 2)
print(marks.reshape(2, 3))

print(marks.reshape(3, 2))