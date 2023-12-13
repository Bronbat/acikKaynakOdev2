

import requests
import json
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():

    url = "http://www.dnd5eapi.co/api/ability-scores/cha"

    response = requests.get(url)

    data = response.json()

    formatted_data = json.dumps(data, indent=4)
    return '<pre>' + formatted_data + '</pre>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6767)
