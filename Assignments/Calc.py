def add(a, b):
 return a + b

def sub(a, b):
 if a >= b:
   return a - b
 else:
   return b-a
def mul(a, b):
 return a * b
def div(a, b):
 if b == 0:
   return "Infinity (division by zero)"
 else:
   return a / b