from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json


class Prices:
    def __init__(self, currency):
        self.url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency'
        self.headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': '312a4a71-566e-4cbe-aea8-538eb53e259c',
        }
        self.currency = currency
        self.session = Session()
        self.session.headers.update(self.headers)

    def fetch(self, url, parameters):
        try:
            response = self.session.get(url, params=parameters)
            data = json.loads(response.text)
            for i in data:
                if i == "data":
                    simplified_data = data[i]
            return simplified_data
        except (ConnectionError, Timeout, TooManyRedirects) as e:
            print(e)

    def get_info(self):
        url = self.url+"/info"
        parameters = {
            'slug':self.currency,
            }
        data = self.fetch(url,parameters)
        return data

    def get_price(self):
        url = self.url + "/listings/latest"
        parameters = {
            'convert':'GBP',
            'limit':'1'
        }
        data = self.fetch(url,parameters)
        return data


if __name__ == "__main__":
    bitcoin = Prices("bitcoin")
    print(bitcoin.get_price())
