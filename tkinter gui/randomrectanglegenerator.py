from tkinter import *
import random
root=Tk()

canvas1=Canvas(root,width=300,height=300)
canvas1.pack()

def randomrect(num):
    for i in range (0,num):
        x1=random.randrange(100)
        y1=random.randrange(100)
        x2=x1+random.randrange(100)
        y2=y1+random.randrange(100)
        canvas1.create_rectangle(x1,y1,x2,y2)

n=int(input("enter the no of rectangles you want : "))

randomrect(n)
root.mainloop()