from flask import Flask, render_template
import requests
import json
import uuid

instance_id = uuid.uuid4().hex
app = Flask(__name__, template_folder='../templates')


@app.route('/')
def index():
    prices = get_price()

    return render_template('index.html', prices = prices, instance=instance_id)


def get_price(crypto_id='polkadot', currency='usd'):
    request_url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto_id}&vs_currencies={currency}"
    response = requests.get(url=request_url)
    res = response.json()
    return res

if __name__ == "__main__":
    app.run(port=5001, host="0.0.0.0")