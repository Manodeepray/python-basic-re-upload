#whene no arguements are given
def myfun():
    for i in range(5):
        print("hi")
        
myfun()



print("2nd function")

#when args are used
def add2num(num1,num2):
    return (num1+num2)

num1=int(input("enter num1: "))

num2=int(input("enter num2: "))
 
res=add2num(num1,num2)
print(res)