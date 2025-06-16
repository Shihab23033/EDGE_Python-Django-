f= open("D:\Codes\EDGE_Python-Django-\Assignments\FileHandaling\write.txt","w") # open the file in write mode 
# This will create the file if it does not exist, or truncate the file to zero length if it does exist.
# f= open("D:\Codes\EDGE_Python-Django-\Assignments\FileHandaling\write.txt","w+") # open the file in write and read mode but this will also truncate the file to zero length if it does exist.
#f= open("D:\Codes\EDGE_Python-Django-\Assignments\FileHandaling\write.txt","a") # open the file in append mode, this will not truncate the file to zero length if it does exist.

data = "This is a sample text written to the file.\nthis will clear the file and write this text to the file.\n"
f.write(data)
f.close()