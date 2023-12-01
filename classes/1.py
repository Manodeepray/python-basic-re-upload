class students:
    def __init__(self,name,grade,age):
        self.name=name
        self.age=age
        self.grade=grade
         
         
student1=students("manodeep","12th",18) 
                     
print(student1.name)
print(student1.grade)
print(student1.age)                     
print("the student's name is "+ student1.name +" his age is "+ str(student1.age) +" he studies in "+student1.grade+"grade")
     
     
     
