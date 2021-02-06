from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects

class News:
    def __init__(self,currency):
        self.url = 