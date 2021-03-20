from flask import Flask
import requests

app = Flask(__name__)


@app.route("/")
def index():
    response = requests.get("https://icanhazip.com")
    return "Hello, World! IP for request was '{0}'.".format(response.json()['origin'])
