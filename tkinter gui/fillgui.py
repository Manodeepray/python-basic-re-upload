from tkinter import *

root=Tk()

thebutton1=Button(None,text="click me!", fg="blue",bg="yellow")
thebutton1.pack()
thebutton2=Button(None,text="hello!", fg="red")
thebutton2.pack(side=LEFT,fill=X)
thebutton3=Button(None,text="hey!", fg="green",bg="yellow" )
thebutton3.pack(side=RIGHT,fill=Y)
thebutton4=Button(None,text="hi!", fg="black")
thebutton4.pack()

root.mainloop()