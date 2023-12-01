from tkinter import *
root = Tk()


label1=Label(root,text="name")
label1.grid(row=0,column=0)
entry1=Entry(root)
entry1.grid(row=0,column=1)

label2=Label(root,text="age")
label2.grid(row=1,column=0)
entry2=Entry(root)
entry2.grid(row=1,column=1)

label3=Label(root,text="gender")
label3.grid(row=2,column=0)
entry3=Entry(root)
entry3.grid(row=2,column=1)

root.mainloop()