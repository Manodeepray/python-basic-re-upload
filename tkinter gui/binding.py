from tkinter import * 
root = Tk()

def printname(event):
    print("hello manodeep")


button1=Button(root,text="click me")
button1.bind("<Up>",printname)
button1.pack()

def leftClick(event):
    print("leftClick")

def rightClick(event):
    print("rightClick")

def scroll(event):
    print("scroll")

def leftKey(event):
    print("leftKey pressed")

def rightKey(event):
    print("rightKey pressed")
    
root.geometry("500x500")

root.bind("<Button-1>",leftClick)
root.bind("<Button-3>",rightClick)
root.bind("<Button-2>",scroll)
root.bind("<Left>",leftKey)
root.bind("<Right>",rightKey)

root.mainloop()