class Students:
    def __init__(self,name,age):
            self.name=name
            self.age=age
    def displayStudents(self):
            return("the student's name is "+ self.name +" his age is "+ str(self.age))

        
         
         
stu=Students("manodeep",19)
stu.displayStudents()