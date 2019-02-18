from flask import Flask
import os

app = Flask(__name__, static_url_path='')


@app.route('/', methods=['GET'])
def root():
    return app.send_static_file('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.environ.get('PORT', 8080))
