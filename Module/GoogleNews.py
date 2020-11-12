import requests
import json
from bs4 import BeautifulSoup

def GoogleNews():
  r=requests.get('https://news.google.com/topstories?tab=rn&hl=zh-TW&gl=TW&ceid=TW:zh-Hant')
  newsData=r.text
  print(newsData)
