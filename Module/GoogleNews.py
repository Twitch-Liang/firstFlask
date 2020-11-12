import requests
import json
from bs4 import BeautifulSoup

r=requests.get('https://news.google.com/topstories?tab=rn&hl=zh-TW&gl=TW&ceid=TW:zh-Hant')
soup=BeautifulSoup(r.text,'html.parser')
print(soup)