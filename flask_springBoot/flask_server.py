from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/tospring")
def spring():
    return "파이썬에서 작성한 내용"

@app.route('/')
def user_juso():
 
    temp = request.args.get('temp', "user")
 
    return "이미지주소: " + temp
    
if __name__ == '__main__':
    app.run(debug=False,host="127.0.0.1",port=5000)