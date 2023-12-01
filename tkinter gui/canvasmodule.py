from tkinter import *
root=Tk()

canvas1=Canvas(root,width=300,height=300)
canvas1.pack()

canvas1.create_rectangle(30,30,100,270)

canvas1.create_line(30,30,100,270)

canvas1.create_polygon(20,20,40,30,200,200)



root.mainloop()