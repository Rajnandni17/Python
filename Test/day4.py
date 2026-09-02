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

#find the product(*) of all digits.
num=int(input("Enter digits:"))
product=1

while num>0:
    digit=num%10
    product=product*digit
    num=num//10
print(product)

#reverse a num.
num=int(input("Enter N:"))
reverse=0

while num>0:
    digit=num%10
    reverse=reverse * 10 + digit
    num=num//10
print(reverse)

#find the first and last digit of a number.
num=int(input("Enter the num:"))
lastdigit=num%10

while num>=10:
    num=num//10
firstdigit=num 
print(lastdigit)
print(firstdigit) 

#check whether num is palindrome.
num=int(input("Enter num:"))

original=num
reverse=0

while num>0:
    digit=num%10
    reverse=reverse * 10 + digit
    num=num//10
    
if original==reverse:
    print("palindrome")
else:
    print("not palindrome")
