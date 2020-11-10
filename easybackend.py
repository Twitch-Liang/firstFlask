from flask import Flask,request
import requests
from bs4 import BeautifulSoup
import json
app = Flask(__name__)

@app.route('/')
def hello_world():
  url = "https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRFZxYUdjU0JYcG9MVlJYR2dKVVZ5Z0FQAQ?hl=zh-TW&gl=TW&ceid=TW%3Azh-Hant"
  r = requests.get(url)
  soup = BeautifulSoup(r.text,"html.parser")
  # 取得頭條新聞的，標題區塊
  titleArea = soup.select(".MQsxIb.xTewfe.R7GTQ.keNKEd.j7vNaf.Cc0Z5d.EjqUne")

  newsDict = {}
  for i,v in enumerate(titleArea):
      #取得標題區塊內的標題
      title = v.select(".DY5T1d")[0].text
      #取得標題區塊內的媒體名稱
      media = v.select(".wEwyrc.AVN2gc.uQIVzc.Sksgp")[0].text
      #取得標題區塊內的新聞連結
      url = "https://news.google.com/" + v.select(".DY5T1d")[0].get("href")
      #取得標題區塊內的內文預覽 ， 利用三元運算過濾空資料情形
      content = v.select('.xBbh9')[0].text if len(v.select('.xBbh9')) else ""
      
      #資料重組
      #如果Key不存在則新增一個Key值為空串列
      if newsDict.get(media) == None :
          newsDict[media] = [] 
      #將資料組合後一次塞入串列
      dataDict = {
          "title":title,
          "href":url,
          "content":content
      }
      newsDict[media].append(dataDict)
      str1 = json.dumps(newsDict,ensure_ascii=False) 
  return str1


if __name__=='__main__':
  app.run(host='127.0.0.1',port=5000)