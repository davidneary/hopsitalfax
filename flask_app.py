
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, request
from flask import Markup
import json
app = Flask(__name__)

@app.route('/')
def hello_world():
    print 'Hello World'
    return 'Hello from Flask!'

@app.route('/', methods=['POST', 'GET'])
def getdata():
    import pdb; pdb.set_trace()
    if request.method == 'POST':
        data = request.json
        print data
        return data
if __name__ == '__main__':
    app.run()

