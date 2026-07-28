# # #Create a list of five fruits
def fruits():
    fruit_list=[]

    for i in range(5):
        fruit=input("enter fruit name:")
        fruit_list.append(fruit)
        print(fruit_list)

fruits()

# #Print the first and last item of a list.
def fruits():
    fruit_list=[]

    for i in range(5):
        fruit=input("enter fruit name:")
        fruit_list.append(fruit)
    print(fruit_list)
    print(fruit_list[0])
    print(fruit_list[-1])
fruits()

# # def fruits():
#     fruit_input = input("Enter fruits separated by commas: ")

#     fruit_list = fruit_input.split(",")

#     print(fruit_list)
#     print(fruit_list[0])
#     print(fruit_list[-1])

# fruits()

# #Add an item to a list.
def item():
    item_list=[]
    
    for i in range(4):
        item=input("enter item name:")
        item_list.append(item)
    print(item_list)
item()

# #Remove an item from a list.
def item():
    item_list=[]
    
    for i in range(4):
        item=input("enter item name:")
        item_list.append(item)
    item_list.pop()
    print(item_list)
item()

# #Sort a list of numbers
def sort_num():
    numbers=[5,8,3,1]
    numbers.sort()
    print(numbers)
sort_num()


#Find the largest number in a list
def find_lar():
    num=[45,23,89,77,2]
    lar=max(num)
    print(lar)
find_lar()

def second_lar():
    numbers=[45,23,89,77,2]
    numbers.sort()
    print(numbers[-2])
second_lar()