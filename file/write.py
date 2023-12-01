
#completely re write
#search for different access modes

f=open('file/pytst.txt','w')
f.write("hello")
f.close
f=open('file/pytst.txt','r')
c=f.read()
print(c)
f.close
