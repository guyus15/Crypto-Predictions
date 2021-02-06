from flask import Flask
from prices import Prices

app = Flask(__name__)

@app.route('/')
def index():
        bitcoin = Prices("bitcoin")
        return bitcoin.get_info()

if __name__ == "__main__":
  app.run()

  