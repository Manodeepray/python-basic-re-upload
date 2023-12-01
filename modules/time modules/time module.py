import time
print(time.time())#no of seconds


def numbers(max):
    time1=time.time()
    for i in range(0,max):
        print(i)
    time2=time.time()
    print("time taken for the code to run")
    print(str(time2-time1))
    
num= int(input("enter the number :"))
numbers(num)

print(time.asctime())

print(time.localtime())

time.sleep(1)#how many second you want the interval between arguements