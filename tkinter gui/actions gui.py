from tkinter import *
root = Tk()
def printname():
    print("hello there manodeep")


button1=Button(root,text="click me!",command=printname)
button1.pack()
root.mainloop()