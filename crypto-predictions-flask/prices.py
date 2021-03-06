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
        self.target_time=datetime.now()
        self.session = Session()
        self.session.headers.update(self.headers)

    def fetch(self, url, parameters):
        current_time = datetime.now()
        
        if current_time < self.target_time:
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

                self.target_time += timedelta(minutes=5)
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
            'limit':'13',
        }
        data = self.fetch(url,parameters)
        for i in data:
            if i.get("name") == self.currency:
                return i


if __name__ == "__main__":
    bitcoin = Prices("Bitcoin Cash")
    print(bitcoin.get_price())
