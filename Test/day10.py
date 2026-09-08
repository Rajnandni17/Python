#Create a dictionary containing a student's name, age and marks, then print each value.
student={
    "name":"raj",
    "age":23,
    "marks":79
}
print(student)

# Count the frequency of every character in a string using a dictionary.
text=input("Enter the text: ")
frequency={}

for chr in text:
    if chr in frequency:
        frequency[chr]+=1
    else:
        frequency[chr]=1

print(frequency)

#Count the frequency of every number in a list.
numbers=list(map(int,input("Enter the values:").split()))
frequency={}

for num in numbers:
    if num in frequency:
        frequency[num]+=1
    else:
        frequency[num]=1
print(frequency)

#Find duplicate elements in a list using a set.
numbers=list(map(int,input("Enter the values:").split()))
duplicate=set()

for num in numbers:
    if numbers.count(num) >1:
        duplicate.add(num)
print(duplicate)    


#Find elements that occur only once in a list.
numbers=list(map(int,input("Enter the values:").split()))
result=[]

for num in numbers:
    if numbers.count(num) ==1:
        result.append(num)
print(result)    

#Find the intersection of two lists using sets.
list1=list(map(int,input("Enter the values of list1:").split()))
list2=list(map(int,input("Enter the values of list2:").split()))

intersection= set(list1) & set(list2)

print(intersection)

#Find the union of two lists using sets.
list1=list(map(int,input("Enter the values of list1:").split()))
list2=list(map(int,input("Enter the values of list2:").split()))


union= set(list1) | set(list2)
print(union)

#Check whether two strings contain the same unique characters
str1=input("Enter the text1: ")
str2=input("enter the text2: ")

if set(str1)==set(str2):
    print("both string have the same unique characters")
else:
    print("string do not have same unique characters")
