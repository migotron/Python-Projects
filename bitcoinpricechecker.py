# Author: Miguel Ibarra【=◈︿◈=】
# Get the current value of a Bitcoin in US dollars using the bitcoincharts api
import requests
import json

def get_bitcoin_price():
    url = 'http://api.bitcoincharts.com/v1/weighted_prices.json'
    response = requests.get(url)
    data = json.loads(response.text)
    return data['USD']['7d']

if __name__ == '__main__':
    print("Bitcoin price: $%s" % get_bitcoin_price())