#Count the num of digits in an integer.
n=int(input("enter N:"))
count=0

while n>0:
    n=n//10
    count+=1
print(count)

#find the sum of all digits of a num.
num=int(input("Enter N:"))
sum=0

while num>0:
    digits= num%10
    sum=sum+digits
    num=num//10
print(sum)