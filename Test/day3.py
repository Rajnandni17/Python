#print nums from 1 to 10.
for i in range(1,11):
    print(i)
    
#print all even nums from 1 to 50.
for i in range(2,51,2):
    print(i)
    
#find the sum of nums from 1 to N.
n= int(input("Enter N: "))
sum=0
for i in range(1,n+1):
    sum+=i
print("Sum of nums from 1 to",n,"is:",sum)

#print the multiplicationtable of a num.
n=int(input("Enter the num:"))

for i in range(1,11):
    print(n,"*",i,"=",n*i)

#count how mmany nums from 1 to N are divisible by 3.
n=int(input("Enter N:"))
count=0
for i in range(1,n+1):
    if i%3==0:
        count+=1
print("Count of nums from 1 to",n,"divisible by 3 is:",count)

#find larger num among N user_entered nums.
n=int(input("Enter N:"))
largest=0
 
for i in range(n):
    num=int(input("Enter value:"))
    if num>largest:
     largest=num
print("largest =",largest)

#cal the product of num from 1 to N without using built in 
n=int(input("Enter num:"))

product=1

for i in range(1,n+1):
    product= product * i
print(product)
