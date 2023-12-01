#frames
 
from tkinter import *

root=Tk()

topframe=Frame(root)
topframe.pack()

botframe=Frame(root)
botframe.pack(side=BOTTOM)

thebutton1=Button(topframe,text="click me!", fg="blue")
thebutton1.pack(side=LEFT)
thebutton2=Button(topframe,text="hello!", fg="red")
thebutton2.pack(side=RIGHT)
thebutton3=Button(botframe,text="hey!", fg="green")
thebutton3.pack(side=LEFT)
thebutton4=Button(botframe,text="hi!", fg="black")
thebutton4.pack(side=RIGHT)

root.mainloop()