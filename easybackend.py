from flask import Flask,request

app = Flask(__name__)    

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = request.get_json()
        print(data)
        print('replyToken:',data[0]['replyToken'])
        print('text:',data[0]['message']['text'])


        return "post"
    if request.method == 'GET':
        return "get"

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=5000)