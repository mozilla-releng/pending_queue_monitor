from flask import Flask
import os
from modules.generate_graphs import generate_html_graphs

app = Flask(__name__)


@app.route('/')
def root():
    generate_html_graphs()
    return app.send_static_file('index.html')


@app.route('/random')
def random():
    return app.send_static_file('random.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.environ.get('PORT', 8080), debug=True)
