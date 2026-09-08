class Student:

    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        print("adding new student in database..")

s1 = Student("karan",88)
print(s1.name,s1.marks)

#create student class that takes name & marks of 3sub as argument in constructor then create a method to print the average>

class Student:
    def __init__(self,name, marks):
        self.name = name
        self.marks = marks


    def get_avg(self):
        sum=0
        for val in self.marks:
            sum += val
        print(self.name,"your avg score is:",sum/3)

s1 = Student("raj",[78,98,86])
s1.get_avg()


#create acc class with 2 attributes :- balance & acc no., create credit, debit & printing thre balance.
class Account:
    def __init__(self,bal,acc):
        self.balance = bal
        self.acc_no = acc
    
    def debit(self,ammount):
        self.balance -= ammount
        print("Rs", ammount,"is debit")
        print("total balance=", self.get_balance())
    
    def credit(self,ammount):
        self.balance += ammount
        print("Rs", ammount,"is credit")
        print("total balance=", self.get_balance())
    
    def get_balance(self):
        return self.balance
    
acc1= Account(10000, 45678)
acc1.debit(567)
acc1.credit(45678)

