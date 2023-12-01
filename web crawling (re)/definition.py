import re
import urllib.request

#https://www.dictionary.com/browse/hel
url="https://www.dictionary.com/browse/"
word=input("enter your word :")
url=url+word
data=urllib.request.urlopen(url).read()
data1=data.decode("UTF-8")

m=re.search('meta data-react-helmet="true" content=',data1)
#print(m)
start=m.end()
end=start+300

newstring=data1[start:end]
#print(newstring)

seemore=re.search("See more",newstring)
finalend=seemore.start()-1
definition=newstring[0:finalend]
print(definition)