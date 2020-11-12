import random


def Fist(text):
    ai = random.randint(0,2)
    player = fist.index(text)
    if ai == player:
      messages=[
          {
              'type':'text',
              'text':'電腦出'+fist[ai]+'，平手'
          },
          {
              "type": "sticker",
              "packageId": "11537",
              "stickerId": "52002773"
          }
      ]               
    elif (ai == 0 and player == 1) or (ai == 1 and player == 2) or (ai == 2 and player ==0):
      messages=[
          {
              'type':'text',
              'text':'電腦出'+fist[ai]+'，您贏了！'
          },
          {
              "type": "sticker",
              "packageId": "11537",
              "stickerId": "52002735"
          } 
      ] 
    else:
      messages=[
          {
              'type':'text',
              'text':'電腦出'+fist[ai]+'，電腦獲勝！'
          },
          {
              "type": "sticker",
              "packageId": "11537",
              "stickerId": "52002734"
          }
      ]
  return messages