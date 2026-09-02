#check whether a num is prime.
num=int(input("Enter num:"))

for i in range(2,num):
    if num%i==0:
        print("Not Prime")
        break
else:
    print("Prime")
    
#print all the prime num from 1 to N.
num=int(input("Enter num:"))
for num in range(2,num+1):
    count=0
    for i in range(1,num+1):
        if num%i==0:
            count+=1
    if count==2:
       print(num)

#calculate factorial of number.
num=int(input("Enter N:"))
factorial=1

for i in range(1,num+1):
    factorial*=i
print("Factorial=",factorial)

#Generate the first N fibonacci num.
num=int(input("Enter the num:"))
a,b=0,1
for i in range(num):
    print(a,end=" ")
    a,b= b,a+b

#check whether a num is an armstrong.
num=int(input("Enter N:"))

original=num
digits=len(str(num))
total=0
while num>0:
    digit=num%10
    total+= digit ** digits
    num//=10
if total== original:
    print("Armstrong number")
else:
    print("Not an armstrong number")

#check whether a num is perfect number.
num=int(input("Enter num:"))
sum=0
for i in range(1,num):
    if num%i==0:
        sum+=i
if sum==num:
    print("Perfect number")
else:
    print("Not perfect number")
    
