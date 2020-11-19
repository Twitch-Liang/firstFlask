from flask_sqlalchemy import SQLAlchemy
from Models import PlayersModel
from flask import Flask

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