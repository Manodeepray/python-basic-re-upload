with open('file/pytst.txt') as file1:
    contents=file1.read()
    print(contents)
    
file2=open('file/pytst.txt','r')
a=file2.read(4)# first parameter in the location 2nd is what  to do with it
print(a)