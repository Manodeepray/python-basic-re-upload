total=10   #global var
def multiply(num1,num2):
    total=num1*num2  #local var: contained within the function
    print(total)
multiply(12,22)

print(total)