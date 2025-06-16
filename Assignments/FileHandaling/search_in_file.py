f= open("D:\Codes\EDGE_Python-Django-\Assignments\FileHandaling\demo.txt","r") # open the file in read mode
data = f.read() # read the entire file
search_term = input("Enter the term to search in the file: ")
if search_term in data:
    print(f"'{search_term}' was found in the file.")
else:
    print(f"'{search_term}' was not found in the file.")