from tkinter import *
root = Tk()
def random():
    print("this is a statement")
    
mainMenu=Menu(root)
root.configure(menu=mainMenu)

submenu=Menu(mainMenu)
mainMenu.add_cascade(label="file",menu=submenu)
submenu.add_command(label="randomm func1",command=random)
submenu.add_command(label="randomm func2",command=random)
submenu.add_command(label="randomm func3",command=random)

submenu.add_separator()
submenu.add_command(label="randomm func4",command=random)

root.mainloop()