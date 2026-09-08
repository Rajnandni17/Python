def type_caller():
   a = input("Enter first value: ")
   b = input("Enter second value: ")

   if a.isalpha() and b.isalpha():
     print("Same datatype")
   elif a.isdigit() and b.isdigit():
      print("Same datatype")
   else:
      print("Different datatype")
type_caller()