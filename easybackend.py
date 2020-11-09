from flask import Flask,request
import requests
from bs4 import BeautifulSoup
import json
app = Flask(__name__)

@app.route('/')
def hello_world():  
  return 'Hello, World!Hello~~~'


if __name__=='__main__':
  app.run(host='127.0.0.1',port=5000)