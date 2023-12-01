from tkinter import *

root=Tk()

equa=""#variable=0
equation=StringVar()

calculation=Label(root,textvariable=equation)
equation.set("Enter your equation")# sets the variable that later changes
calculation.grid(columnspan=4)

def btnpress(num):
    global equa
    equa=equa+str(num)
    equation.set(equa) #equation = equa ie 0 or ....
    
Button0=Button(root,text="0",command=lambda:btnpress(0))       
Button0.grid(row=4,column=1)    

Button1=Button(root,text="1",command=lambda:btnpress(1))       
Button1.grid(row=1,column=0)        

Button2=Button(root,text="2",command=lambda:btnpress(2))       
Button2.grid(row=1,column=1)        

Button3=Button(root,text="3",command=lambda:btnpress(3))       
Button3.grid(row=1,column=2)    

Button4=Button(root,text="4",command=lambda:btnpress(4))       
Button4.grid(row=2,column=0)        

Button5=Button(root,text="5",command=lambda:btnpress(5))       
Button5.grid(row=2,column=1)        

Button6=Button(root,text="6",command=lambda:btnpress(6))       
Button6.grid(row=2,column=2)    

Button7=Button(root,text="7",command=lambda:btnpress(7))       
Button7.grid(row=3,column=0)        

Button8=Button(root,text="8",command=lambda:btnpress(8))       
Button8.grid(row=3,column=1)        

Button9=Button(root,text="9",command=lambda:btnpress(9))       
Button9.grid(row=3,column=2)        

Buttonplus=Button(root,text="+",command=lambda:btnpress("+"))       
Buttonplus.grid(row=1,column=3)        

Buttonminus=Button(root,text="-",command=lambda:btnpress("-"))       
Buttonminus.grid(row=2,column=3)        

Buttonmultiply=Button(root,text="x",command=lambda:btnpress("*"))       
Buttonmultiply.grid(row=3,column=3)        

Buttondivide=Button(root,text="/",command=lambda:btnpress("/"))       
Buttondivide.grid(row=4,column=3)  


def equalpress():
    global equa
    answer=str(eval(equa))
    equation.set(answer)
    

Buttonequal=Button(root,text="=",command=equalpress)       
Buttonequal.grid(row=4,column=2)   

def clear():
    global equa
    equa=""
    equation.set(equa)     
      
Buttonequal=Button(root,text="C",command=clear)       
Buttonequal.grid(row=4,column=0)


root.mainloop()