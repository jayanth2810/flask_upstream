__author__ = 'jayanthvenkataraman'

from flask import Flask
import os

app = Flask(__name__)


@app.route('/refund', methods = ['GET'])
def login_function():
    return "Refund Successfully Initiated"

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000)) #for taking Heroku's PORT environment variable
    app.run(host='0.0.0.0', port=port)