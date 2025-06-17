n=int(input("n= "))
a = list(map(int, input(f"Enter {n} numbers: ").split()))
s=""
for i in range(n):
    x=int(a[i])
    s +=str( x%10)
num=int(s)
if num%10 == 0:
    print("Yes")
else:
    print("No")