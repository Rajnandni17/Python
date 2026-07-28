#Create a set of numbers.
def name_set():
    my_set={"raj","tanu","jaijeet","rishi"}
    print(my_set)
name_set()

#Add an item to a set.
def item_set():
    my_set={"car","keys","house","fruits"}
    my_set.add("toys")
    print(my_set)
item_set()

#remove an item from a set.
def item_set():
    my_set={"car","keys","house","fruits"}
    my_set.remove("keys")
    print(my_set)
item_set()

#Find common elements between two sets.
def common_num():
    set1={"11","34","76","54"}
    set2={"34","66","90"}
    result=set1.intersection(set2)
    print(result)
common_num()