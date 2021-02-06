from flask import Flask, request, render_template, jsonify
from prices import Prices

app = Flask(__name__)

@app.route('/getinfo')
def get_info():
        currency = request.args.get('currency')
        print("Currency: " + currency)
        currency_info = Prices(currency)
        return jsonify(currency_info.get_info())

@app.route('/getprice')
def get_price():
        currency = request.args.get('currency')
        print("Currency: " + currency)
        current_price = Prices(currency)
        return jsonify(current_price.get_price())

if __name__ == "__main__":
  app.run()

  