#pramanent data store
def login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    found = False

with open("system\\user.txt", "r") as file:
    for line in file:
        user, pwd = line.strip().split(",")

        if username == user and password == pwd:
            found = True
            break

if found:
    print("Login successful!")
else:
    print("Login failed!")




    
#temporary data store
def login():
    username=input("create name:")
    password=input("create password:")

    user=input("enter name:")
    pwd=input("enter password:")
    if user==username and password==pwd:
       print("valid login")

    else:
        print("invalid login")

login()