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
    crypto = {'bitcoin':'usd'}
    crypto[crypto_id] = currency
    ans = []
    for k,v in crypto.items():
        request_url = f"https://api.coingecko.com/api/v3/simple/price?ids={k}&vs_currencies={v}"
        response = requests.get(url=request_url)
        res = response.json()
        ans.append(res)
    return ans

if __name__ == "__main__":
    app.run(port=5001, host="0.0.0.0")