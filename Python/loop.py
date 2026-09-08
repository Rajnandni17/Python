#for loop
n=5
for i in range (0,n):
    print(i)

#index of sequences
a= ["geeks", "for","geeks"]
for idx in range(len(a)):
    print(a[idx])

#while loop
cnt=0
while(cnt<6):
    cnt=cnt+1
    print("hello geek")

#nested loop
for i in range(1,5): #Outer loop (i) → decides which number to print.
    for j in range(i): #Inner loop (j) → decides how many times to print that number
        print(i,end='')
    print()
    