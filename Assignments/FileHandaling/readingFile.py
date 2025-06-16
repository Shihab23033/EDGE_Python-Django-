f=open("D:\Codes\EDGE_Python-Django-\Assignments\FileHandaling\demo.txt","r") # open the file in read mode
# f=open("D:\Codes\EDGE_Python-Django-\Assignments\FileHandaling\demo.txt","r+") # open the file in read and write mode

data=f.read() # read the entire file
# data=f.readline() # read the first line of the file
# # data=f.readlines() # read all lines of the file and return a list
# f.seek(0) # move the cursor to the beginning of the file
# # data=f.read(10) # read the first 10 characters of the file  

print(data)
f.close()
'''
# another way to read a file is using the with statement
with open("D:\Codes\EDGE_Python-Django-\Assignments\FileHandaling\demo.txt", "r") as f:
    data = f.read()
    print(data)

'''