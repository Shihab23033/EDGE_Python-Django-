def SeriesSum(n):
    return n * (n + 1) // 2 

n = int(input("Enter the value of n: "))

sum= SeriesSum(n)
print(f"Sum of the series 1 + 2 + ... + {n} = {sum}")
