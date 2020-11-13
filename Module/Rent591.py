import requests
from bs4 import BeautifulSoup
import json

url='https://rent.591.com.tw/?kind=0&region=8'
r= requests.get(url)

soup=BeautifulSoup(r.text,'html.parser')

houseCards=soup.select('.listInfo')

for houseInfo in houseCards:
  imageUrl = houseInfo.select('.imageBox img')[0].get('data-original')
  titleArea = houseInfo.select('.infoContent h3 a')[0]
  title = titleArea.text
  infoUrl = 'https:'+titleArea.get('herf')
  print(imageUrl,'\n')