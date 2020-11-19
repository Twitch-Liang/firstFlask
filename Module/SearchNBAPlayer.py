from flask_sqlalchemy import SQLAlchemy
from Models import PlayersModel
from flask import Flask
from flask import request
import os
db = SQLAlchemy()

app = Flask(__name__)

URL=os.environ.get('DATABASE_URL', None)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = URL


db.init_app(app)

def SearchNBAPlayer(text):
  name = text.split('/')[1]
  # print(time.now)
  # query = PlayersModel.query.filter_by(name=name).first()
  # print(time.now)
  query = PlayersModel.query.filter(PlayersModel.name.ilike("%" + name + "%")).first()
  if query != None:
      messages =[
          {
          'type':'text',
          'text': f'{query.name}:{query.from_}~{query.to_}'
          }
      ]
  else:
        messages =[
          {
          'type':'text',
          'text': f'對不起！我沒找到與{name}相關的資料QxQ'
          }
      ]
  return messages