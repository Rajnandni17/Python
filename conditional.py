#if condition
age=19
if age >=18:
    print("eligible to vote.")

#if else
age=18
if age<=20:
    print("travel for free.")
else:
    print("pay for ticket.")

#if-elif-else statement
age=27

if age <=12:
    print("child.")
elif age <=19:
    print("teenager.")
elif age<=30:
    print("young adult.")
else:
    print("adult.")

#nested if statement
age =50
is_member =True

if age>=45:
    if is_member:
        print("30% senior discount!")
    else:
            print("20% senior discount.")

else:
    print("not eligible for a senior discount.")


