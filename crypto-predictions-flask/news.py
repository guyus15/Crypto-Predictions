from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects

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
        #data = json.loads(response.text)
        print(response.text)



if __name__ == "__main__":
    bitcoin = News("Bitcoin")
    bitcoin.get_news()