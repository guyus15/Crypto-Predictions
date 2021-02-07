from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

class News:
    def __init__(self,currency):
        self.url = "https://api.thenewsapi.com/v1/news/top?api_token=LbcHmUn9gxYNw513YxaXKFifpvILBx2xayLlpw90"
        self.session = Session()
        self.currency = currency



    def get_news(self):
        parameters = {
            "search":self.currency,
            "language":"en",
            "exclude_categories":"sport, entertainment, food, travel"
        }
        response = self.session.get(self.url, params=parameters)
        simplified_data = []
        data = json.loads(response.text)
        for i in data:
            if i == "data":
                simplified_data.append(data[i])
        return simplified_data



if __name__ == "__main__":
    bitcoin = News("Bitcoin")
    bitcoin.get_news()