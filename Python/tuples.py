#Create a tuple of five numbers.
def num_tuple():
    temp_list=[]
    
    for i in range(5):
        num=input("enter value:")
        temp_list.append(num)
    my_tuple=tuple(temp_list)
    print(my_tuple)
num_tuple()

#Print the second item of a tuple.
def num_tuple():
    my_tuple=("5","8","2","1","0")
    
    print(my_tuple)
    print(my_tuple[1])
num_tuple()

#Find the length of a tuple.
def num_tuple():
    my_tuple=("5","8","2","1","0","3","4")
    
    print(len(my_tuple))
num_tuple()

#Convert a tuple into a list.
def tuple_to_list():
    my_tuple=("keys","house","gun","cars","toys")
    my_list=list(my_tuple)
    print(my_tuple)
    print(my_list)
tuple_to_list()

#Check if an item exists in a tuple
def item_exists():
    my_tuple=("11","56","8","0","33")

    if "8" in my_tuple:
        print("exists")
    else:
        print("not exists")
item_exists()

