from tkinter import *
root=Tk()

label1=Label(root,text="enter your expression")
label1.pack()

def evaluate(event):
    data=E.get()
    ans.configure(text="answer :"  + str(eval(data)))

E=Entry(root)

ans=Label(root)
ans.pack()

E.bind("<Return>",evaluate)
E.pack()

root.mainloop()