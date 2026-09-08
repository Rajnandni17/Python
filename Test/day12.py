# Reverse a list using two pointers.
numbers=list(map(int,input("Enter the elements:").split()))
left=0
right=len(numbers)-1

while left< right:
    numbers[left],numbers[right]=numbers[right],numbers[left]
    
    left+=1
    right-=1
print(numbers)

#Check whether a list is a palindrome using two pointers.
numbers=list(map(int,input("Enter the elements:").split()))
left=0
right=len(numbers)-1

while left < right:
    if numbers[left] != numbers[right]:
        print("Not palindrome")
        break
    
    left+=1
    right-=1
else:
        print("Palindrome")


#Check whether a string is a palindrome using two pointers.
text=input("Enter the text:")
left=0
right=len(text)-1

while left < right:
    if text[left] != text[right]:
        print("Not palindrome")
        break
    
    left+=1
    right-=1
else:
        print("Palindrome")   