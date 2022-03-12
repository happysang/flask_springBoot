from flask import Flask

import urllib.request

app = Flask(__name__)

@app.route("/tospring")
def spring():
    
    return "파이썬에서 작성한 내용"
    
    
if __name__ == '__main__':
    app.run(debug=False,host="127.0.0.1",port=5000)