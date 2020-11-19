import requests
import json
from bs4 import BeautifulSoup

r=requests.get('https://news.google.com/topstories?tab=rn&hl=zh-TW&gl=TW&ceid=TW:zh-Hant')
soup=BeautifulSoup(r.text,'html.parser')
# print(soup)
dataArea=soup.select('.ipQwMb.ekueJc.RD0gLb')
for i in dataArea:
  title=i.select('.DY5T1d')[0].text
  linkData=i.select('.DY5T1d')[0].get('href')
  url='https://news.google.com/'+linkData
  print(url)