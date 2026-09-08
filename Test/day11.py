#Count elements greater than X.
numbers=list(map(int,input("Enter the elements:").split()))
X=30
count=0
for num in numbers:
    if num >X:
        count+=1
print("Count=",count)

#Find first occurrence of a target.
numbers=list(map(int,input("Enter the elements:").split()))
target=int(input("Enter target:"))

for i in range(len(numbers)):
    if numbers[i]==target:
        print("First occurrence=",i)
        break
  
#find last occurrence of a target.
numbers=list(map(int,input("Enter the elements:").split()))
target=int(input("Enter target:"))
position= -1

for i in range(len(numbers)):
    if numbers[i]==target:
        position=i
print("last occurrence=",position)

#Find the difference between largest and smallest.
numbers=list(map(int,input("Enter the elements:").split()))

largest= numbers[0]
smallest=numbers[0]

for num in numbers:
    if num > largest:
        largest= num
    if num< smallest:
        smallest= num
difference= largest - smallest
print("difference is=",difference)       
    