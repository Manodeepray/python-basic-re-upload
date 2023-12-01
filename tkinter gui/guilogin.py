from tkinter import *
root = Tk()


label1=Label(root,text="Name:")
label1.grid(row=0,column=0,sticky="E")
entry1=Entry(root)
entry1.grid(row=0,column=1)

label2=Label(root,text="Password:")
label2.grid(row=1,column=0,sticky="E")
entry2=Entry(root)
entry2.grid(row=1,column=1)

checkbutton2=Checkbutton(root,text="Remember Password")
checkbutton2.grid(columnspan=2)
root.mainloop()