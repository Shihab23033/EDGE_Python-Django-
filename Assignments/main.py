import Calc as c
a = int(input("Enter a:"))
b = int(input("Enter b:"))

while True:
 choice = int(input("Enter 1 to add and 2 to sub 3 to mul 4 to div or -1 to exit:"))


 if choice == -1:
  print("Exiting program.")
  break

 elif choice == 1:
  print(a," + ", b," = ", c.add(a, b))
 elif choice == 2:
  print(a," - ", b," = ", c.sub(a, b))
 elif choice ==3:
  print(a," * ", b," = ", c.mul(a, b))
 elif choice == 4:
  print(a," / ", b," = ", c.div(a, b))