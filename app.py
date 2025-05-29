from flask import Flask, jsonify
import requests
import os

app = Flask(__name__)

@app.route('/')
def home():
    return 'CJ Proxy is running.'

@app.route('/token', methods=['GET'])
def get_token():
    url = "https://developers.cjdropshipping.com/authentication/getAccessToken"
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "cjAccessKey": os.environ.get('CJ_ACCESS_KEY'),
        "cjSecret": os.environ.get('CJ_SECRET')
    }

    response = requests.post(url, json=data, headers=headers)
    return jsonify(response.json())

if __name__ == '__main__':
    import os
port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)

