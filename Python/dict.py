#Create a dictionary with student details.
def student_dict():
    student={
        "name":"jaijeet",
        "age":20,
        "city":"italy"
    }
    print(student)

student_dict()

#Access a value using its key
def access_value():
    student={
        "name":"jaijeet",
        "age":20,
        "city":"italy"
    }
    print(student["name"])
    print(student["city"])
access_value()

#Add a new key-value pair.
def new_key():
    student={
        "name":"jaijeet",
        "age":20,
    }
    student["city"]="jalandhar"
    print(student)
new_key()

#Update an existing value.
def update_value():
    student={
        "name":"jaijeet",
        "age":20,
    }
    student["age"]=int(input("enter a new age:"))
    print(student)
update_value()

#Delete an item from a dictionary.
def del_value():
    student={
        "name":"jaijeet",
        "age":20,
        "city":"jalandhar"
    }
    del student["age"]
    print(student)
del_value()