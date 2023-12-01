class Student:
    def __init__(self,name,age):
         self.name=name
         self.age=age
student1=Student("manodeep",17)
student2=Student("BOB",12)
x=hasattr(student1,'age')
print("x: "+str(x))
y=hasattr(student2,'grade') #check if the attribute is present or not
print("y :" + str(y))

z=getattr(student1,'age') #get the value as typeset it was defined
print("z= "+str(z))
setattr(student2,'grade','8th') #create attribute
w=hasattr(student2,'grade')
print("w="+str(w))
delattr(student1,'name') # delete attribute
t=hasattr(student1,'name')
print("t= "+str(t))