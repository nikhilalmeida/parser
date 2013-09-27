#!flask/bin/python
from flask import Flask
import parser

app = Flask(__name__)

@app.route('/todo/api/v1.0/email', methods = ['POST'])
def index():
        return parser.parse()

if __name__ == '__main__':
    app.run(debug = True)
