#Count the number of characters in a string without using a built-in count of length
text=input("Enter the string:")
count=0
for chr in text:
    count+=1
print(count)

#Count vowels in a string
text=input("Enter the string:")
count=0
for chr in text:
    if chr in"aeiouAEIOU":
        count+=1
print(count)

# Reverse a string without using slicing.
text = input("Enter a string: ")
reverse = ""

for i in range(len(text) - 1, -1, -1):
    reverse = reverse + text[i]

print("Reversed string =", reverse)

#Count vowels and consonants separately
text = input("Enter a string: ")

vowels = 0
consonants = 0

for ch in text:
    if ch in "aeiouAEIOU":
        vowels = vowels + 1
    elif ch.isalpha():
        consonants = consonants + 1

print("Vowels =", vowels)
print("Consonants =", consonants)

#Count how many times a particular character appears.
name = "banana"
print(name.count("a"))

#Remove all spaces from a string
name = "  Python  "
print(name.strip())

#Find the first character that appears more than once
text = input("Enter a string: ")

for ch in text:
    if text.count(ch) > 1:
        print("First repeated character =", ch)
        break
    
#Check whether two strings are anagrams.   
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

if sorted(str1) == sorted(str2):
    print("Strings are anagrams")
else:
    print("Strings are not anagrams")