# Shamelessly copied from http://flask.pocoo.org/docs/quickstart/

from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'index page!wbhook added'

@app.route('/hello')
def hello_world():
    return 'Hello World!from docker'
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug = True)
