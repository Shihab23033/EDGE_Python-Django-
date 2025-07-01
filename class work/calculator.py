from tkinter import *
class Calculator:
    def __init__(self,win):
        self.win = win
        self.win.title("Calculator")
        self.win.geometry("700x500")
        self.num1 =Label(win,text="enter first number", font=("Arial", 20))
        self.num1.place(x=50, y=50)
        self.num2 =Label(win,text="enter second number", font=("Arial", 20))
        self.num2.place(x=50, y=150)
        self.res = Label(win, text="Result", font=("Arial", 20))
        self.res.place(x=50, y=350)
        self.box1 = Entry(win, font=("Arial", 20))
        self.box1.place(x=350, y=50)
        self.box2 = Entry(win, font=("Arial", 20))
        self.box2.place(x=350, y=150)
        self.res_box = Entry(win, font=("Arial", 20))
        self.res_box.place(x=200, y=350)
        self.add = Button(win, text="+", font=("Arial", 20,), command=self.ADD)
        self.add.place(x=50, y=250)
        self.sub = Button(win, text="-", font=("Arial", 20,), command=self.SUB)
        self.sub.place(x=150, y=250)
        self.mul = Button(win, text="x", font=("Arial", 20,), command=self.MUL)
        self.mul.place(x=250, y=250)
        self.div = Button(win, text="/", font=("Arial", 20,), command=self.DIV)
        self.div.place(x=350, y=250)
        self.mod = Button(win, text="MOD", font=("Arial", 20,), command=self.MOD)
        self.mod.place(x=450, y=250)
    def ADD(self):
        num1 = int(self.box1.get())
        num2 = int(self.box2.get())
        result = num1 + num2
        self.res_box.delete(0, END)
        self.res_box.insert(0, str(result))
    def SUB(self):
        num1 = int(self.box1.get())
        num2 = int(self.box2.get())
        result = num1 - num2
        self.res_box.delete(0, END)
        self.res_box.insert(0, str(result))
    def MUL(self):
        num1 = int(self.box1.get())
        num2 = int(self.box2.get())
        result = num1 * num2
        self.res_box.delete(0, END)
        self.res_box.insert(0, str(result))
    def DIV(self):
        num1 = int(self.box1.get())
        num2 = int(self.box2.get())
        if num2 == 0:
            self.res_box.delete(0, END)
            self.res_box.insert(0, "Error")
        else:
            result = num1 / num2
            self.res_box.delete(0, END)
            self.res_box.insert(0, str(result))
    def MOD(self):
        num1 = int(self.box1.get())
        num2 = int(self.box2.get())
        result = num1 % num2
        self.res_box.delete(0, END)
        self.res_box.insert(0, str(result))
if __name__ == "__main__":
    win = Tk()
    calc = Calculator(win)
    win.mainloop()