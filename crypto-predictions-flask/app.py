from flask import Flask, request, render_template, jsonify
from prices import Prices
from flask_sqlalchemy import SQLAlchemy

 

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///crypto_data.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SECRET_KEY"] = "SECRETKEY"
db = SQLAlchemy(app)

class currency_info(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True)
    symbol = db.Column(db.String(5), unique=True)
    logo = db.Column(db.String(30))
    description = db.Column(db.String(300))
    last_updated = db.Column(db.String(20))
    date_added = db.Column(db.String(20))
    website = db.Column(db.String(30))
    technical_doc = db.Column(db.String(30))


@app.route('/getinfo')
def get_info():
        currency = request.args.get('currency')
        print("Currency: " + currency)
        coin = currency_info.query.filter_by(name=currency).first()
        json_string = "{" + "name:"+coin.name +"," + "symbol:"+coin.symbol + "," + "description:"+coin.description + "," + "date_added:"+coin.date_added + "," + "website:"+coin.website + "}"
        #currency_info = Prices(currency)
        #return jsonify(currency_info.get_info())
        return jsonify(json_string)

@app.route('/getprice')
def get_price():
        currency = request.args.get('currency')
        print("Currency: " + currency)
        current_price = Prices(currency)
        return jsonify(current_price.get_price())

if __name__ == "__main__":
  app.run()

  