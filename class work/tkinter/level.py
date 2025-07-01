from tkinter import *
r= Tk() #create a tk object / window
r.title("Title")
#r.geometry("300x200")   
label = Label(r, text="Welcome to the Level Window")
label.pack()
button = Button(r, text="Close",width=40, height=20 , command=r.destroy)
button.pack() 
r.mainloop()