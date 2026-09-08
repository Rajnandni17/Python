# Find the largest element in a list without using max().
numbers=list(map(int, input("Enter the value:").split()))

largest= numbers[0]

for num in numbers:
    if num>largest:
        largest=num
print("Largest=",largest)


#Find the smallest element without using min()
numbers=list(map(int, input("Enter the value:").split()))

smallest= numbers[0]

for num in numbers:
    if num < smallest:
        smallest=num
print("smallest=",smallest)

#Calculate the sum of list elements without using sum().
numbers=list(map(int, input("Enter the value:").split()))

total=0

for num in numbers:
    total+=num
print("Sum=",total)


#Count even and odd numbers in a list. 
numbers=list(map(int, input("Enter the value:").split()))
even_count=0
odd_count=0
for num in numbers:
    if num%2==0:
        even_count+=1
    else:
        odd_count+=1
print("Even=",even_count)
print("Odd=",odd_count)

#Reverse a list without using reverse().
numbers=list(map(int, input("Enter the value:").split()))    

for i in range(len(numbers)-1,-1,-1):
    print(numbers[i],end=" ")


#remove duplicates from a list.
numbers=list(map(int, input("Enter the value:").split())) 

unique=[]

for num in numbers:
    if num not in unique:
        unique.append(num)
print(unique)

#Find the second largest element in a list.
numbers=list(map(int, input("Enter the value:").split())) 

largest=numbers[0]
second=numbers[0]

for num in numbers:
    if num > largest:
        second=largest
        largest=num
    elif num > second and num !=largest:
        second= num
print("Second largest=", second)


#Search for a given element and return its position.
numbers=list(map(int, input("Enter the value:").split())) 

element=int(input("Enter the element to search:"))

for i in range(len(numbers)):
    if numbers[i]==element:
        print("Position=",i)
        break
    
#Move all zeroes in a list to the end while keeping the other elements in their original order.
numbers=list(map(int, input("Enter the value:").split())) 
result=[]

for num in numbers:
    if num !=0:
        result.append(num)

for num in numbers:
    if num==0:
        result. append(num)

print(result)        