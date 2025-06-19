import math as m

def e_x( x, n):
    res= 0.0
    for i in range(n + 1):
        res += (x ** i) / m.factorial(i)    
    return res
def error_e_x(x, n):
    return abs(m.e**x - e_x(x, n))

if __name__ == "__main__":
    rf= open("D:\Codes\EDGE_Python-Django-\Assignments\input.txt", "r")
    wf= open("D:\Codes\EDGE_Python-Django-\Assignments\output.txt", "w")
    line= rf.readline()
   # print(line)
    
    while line != "":
        x, n= map(int, line.split())
        wf.write(f"Actual value of e^{x} = {m.e**x}\n")
        wf.write("term\t\tmaclourin\t\terror\n")
        for i in range(1, n + 1):
            result= e_x(x, i)
            error= error_e_x(x, i)
            wf.write(f"{i}\t\t\t{result:.03f}\t\t\t{error:.03f}\n")
        wf.write("\n")  
        line= rf.readline()
    print("Output written to output.txt")
    rf.close()
    wf.close()