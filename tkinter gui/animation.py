from tkinter import *
root=Tk()
import time

canvas1=Canvas(root,width=300,height=300)
canvas1.pack()

canvas1.create_polygon(10,10,10,60,50,35)

for i in range(0,60):
    canvas1.move(1,5,0)
    root.update()
    time.sleep(0.1)

root.mainloop()