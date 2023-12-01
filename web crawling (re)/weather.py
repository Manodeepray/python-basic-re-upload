import re
import urllib.request
#https://www.google.com/search?q=bhubaneshwar+weather&rlz=1C1PRFI_enIN1022IN1022&oq=bhubaneshwar+weather&aqs=chrome..69i57j0i512j46i512j0i512l2j0i10i433i512j69i60l2.8613j0j4&sourceid=chrome&ie=UTF-8
city=input("enter your city:")
url="https://www.google.com/search?q="+city+"+weather&rlz=1C1PRFI_enIN1022IN1022&oq="+city+"+weather&aqs=chrome..69i57j0i512j46i512j0i512l2j0i10i433i512j69i60l2.8613j0j4&sourceid=chrome&ie=UTF-8"
print(url)
data=urllib.request.urlopen(url).read()
data1= data.decode("UTF-8")

print(data1)
