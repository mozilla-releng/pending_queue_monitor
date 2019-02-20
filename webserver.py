import os
from flask import Flask

app = Flask(__name__)


@app.route('/')
def root():
    return app.send_static_file("index.html")


@app.route('/random')
def random():
    return app.send_static_file('random.html')


@app.route('/releng')
def releng():
    return app.send_static_file('releng.html')


@app.route('/aws')
def aws():
    return app.send_static_file('aws.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.environ.get('PORT', 8080), debug=True)
