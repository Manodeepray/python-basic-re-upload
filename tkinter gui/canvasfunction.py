from tkinter import *
root=Tk()

canvas1=Canvas(root,width=300,height=300)
canvas1.pack()

def createRect(x1,y1,x2,y2):
    canvas1.create_rectangle(x1,y1,x2,y2,fill="blue")
    
    
createRect(5,50,200,70)  
    
createRect(55,54,33,22)
root.mainloop()