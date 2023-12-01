import re
import urllib.request
#https://www.google.com/finance/quote/
stock=input("enter your stock :")
url = "https://www.google.com/finance/quote/"+stock+":NASDAQ"
print(url)

data=urllib.request.urlopen(url).read()

data1=data.decode("UTF-8")

m = re.search('meta itemprop="price"', data1)
start = m.start()
end = start + 50
newString = data1[start:end]
m = re.search('content="', newString)
start = m.end()
newString1 = newString[start:]
m = re.search("/", newString1)
start = 0
end = m.end()-3
final = newString1[0:end]
print("The value of " + stock.upper() + " is " + final)