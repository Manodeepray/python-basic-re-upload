from tkinter import *
import tkinter.messagebox

root=Tk()

tkinter.messagebox.showinfo("Window Title ","did i did i did i did i")

answer=tkinter.messagebox.askquestion("question 1","are you human")
if answer=="yes":
    tkinter.messagebox.showinfo("congrats","kill urself")
if answer=="no":
    tkinter.messagebox.showinfo("alien","go to area 51")


root.mainloop()