a=1
n=input("Enter a number: ")
n=int(n)
sum=0
while a<=n*2-1:
   # print(a**2, end="+")
    sum+=a**2
    a+=2

print("\nSum of squares of first", n, "odd numbers is:", sum)