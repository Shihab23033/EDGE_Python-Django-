import ImgCalc as im

class main:
    def __init__(self):
        pass
    if(__name__=="__main__"):
        a=complex(input("enter 1st number: "))
        b=complex(input("enter 2nd number: "))

        obj=im.ImgCalc(a,b)
        op=input("enter the operation you want to perform: ")
        print(a,op,b,"=",obj.Calc(op))

