import requests
from bs4 import *
data=requests.get("https://www.accuweather.com/en/in/bhubaneswar/1-189781_1_al/weather-forecast/1-189781_1_al")
soup = BeautifulSoup(data.text,"html.parser")

print(soup.find('script' ))