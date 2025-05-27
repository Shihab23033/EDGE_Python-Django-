word= ["dhaka","rajshahi", "tangail"]
for i in word:
    print(i)

print("\nReverse order")
for i in range(len(word)-1,-1,-1):
    print(word[i])

print("\nReverse order another way")
for i in range(1,len(word)+1):
    print(word[i*-1])

