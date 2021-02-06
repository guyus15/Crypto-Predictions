from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from datetime import datetime, timedelta
import time

class Prices:
    def __init__(self, currency):
        self.url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency'
        self.headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': '312a4a71-566e-4cbe-aea8-538eb53e259c',
        }
        self.currency = currency
        self.last_call_time=datetime.now() + timedelta(minutes=6)
        self.session = Session()
        self.session.headers.update(self.headers)

    def fetch(self, url, parameters):
        self.current_time = datetime.now()
        print(self.current_time)
        print(self.last_call_time)
        print(self.current_time-self.last_call_time)
        if self.last_call_time + timedelta(minutes=5) > self.current_time:
            print("Time between calls too recent")
            return
        else:
            try:
                response = self.session.get(url, params=parameters)
                data = json.loads(response.text)
                self.last_call_time = data.get("status").get("timestamp")
                self.last_call_time = self.last_call_time.replace("T"," ")
                self.last_call_time = self.last_call_time[:-1]
                self.last_call_time = datetime.strptime(self.last_call_time, "%Y-%m-%d %H:%M:%S.%f")
                print("new time: ",self.last_call_time)
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
    bitcoin.get_price()
    time.sleep(5)
    bitcoin.get_price()