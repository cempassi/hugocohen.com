# Flask web application test

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hey, We have a working app, yeah baby!'

if __name__ == '__main__' :
    app.run(debug=True, host='0.0.0.0')
