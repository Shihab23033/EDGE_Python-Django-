def f(ann1:str, ann2: str) -> str:
    """
    This function takes two strings as input and returns a string.
    """
    print("annotation", f.__annotations__)
    print("arguments:",ann1, ann2)
    return ann1 +" "+ ann2
print(f('hello', 'world'))