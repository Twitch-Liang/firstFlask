from flask import Flask,request
import requests
from bs4 import BeautifulSoup
import json
app = Flask(__name__)

@app.route('/')
def hello_world():  
  return 'Hello, World!Hello~~~'

@app.route('/one')
def my_name_is():  
  return 'Twitch,Liang'

@app.route('/two')
def test():
  a = 1
  b = 2
  c = a+b  
  return str(c)

@app.route('/three',methods=['GET', 'POST'])
def news():
  if request.method == 'POST':
    return "post"
  else:
    url = "https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRFZxYUdjU0JYcG9MVlJYR2dKVVZ5Z0FQAQ?hl=zh-TW&gl=TW&ceid=TW%3Azh-Hant"
    r = requests.get(url)
    soup = BeautifulSoup(r.text,"html.parser")
    titleArea = soup.select(".MQsxIb.xTewfe.R7GTQ.keNKEd.j7vNaf.Cc0Z5d.EjqUne")

    newsDict = {}
    for i,v in enumerate(titleArea):   
        title = v.select(".DY5T1d")[0].text   
        media = v.select(".wEwyrc.AVN2gc.uQIVzc.Sksgp")[0].text  
        url = "https://news.google.com/" + v.select(".DY5T1d")[0].get("href")
        content = v.select('.xBbh9')[0].text if len(v.select('.xBbh9')) else ""
        

        if newsDict.get(media) == None :
            newsDict[media] = [] 

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