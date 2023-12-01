class parents:
    counter=10
    def __init__(self):
        print("class initialised")
    def parentfunc(self):
        print("parentfunc called")
    def setcount(self,num):
        parents.counter=num
    def showcount(self):
        print(str(parents.counter))
           
class child():
    def __init__(self):
        print("child class being initialised")
    def childfunc(self):
        print("childfunc being called")   
class child(parents):
    def __init__(self):
        print("child class being initialised")
    def childfunc(self):
        print("childfunc being called")           
    
    
print(child.setcount(100))
