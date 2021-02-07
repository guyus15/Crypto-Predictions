from flask import Flask, request, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from prices import Prices
#from tables import currency_prices, currency_news
import json


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

class currency_prices(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    last_updated = db.Column(db.String(20))
    price = db.Column(db.Integer)
    percent_change_1h = db.Column(db.Integer)
    percent_change_24h = db.Column(db.Integer)
    percent_change_7d = db.Column(db.Integer)
    discriminator = db.Column(db.String(50))
    __mapper_args__ = {'polymorphic_on': discriminator}

class currency_news(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(40))
    last_updated = db.Column(db.String(20))
    title = db.Column(db.String(30))
    content = db.Column(db.String(2000))
    url = db.Column(db.String(150))
    image_url = db.Column(db.String(150))
    published = db.Column(db.String(20))
    discriminator = db.Column(db.String(50))
    __mapper_args__ = {'polymorphic_on': discriminator}


class bitcoin_prices(currency_prices, db.Model):
    __tablename__ = "bitcoin_prices"
    __mapper_args__ = {'polymorphic_identity': 'bitcoin_prices'}

class bitcoin_news(currency_news, db.Model):
    __tablename__ = "bitcoin_news"
    __mapper_args__ = {'polymorphic_identity': 'bitcoin_news'}

class ethereum_prices(currency_prices, db.Model):
    __tablename__ = "ethereum_prices"
    __mapper_args__ = {'polymorphic_identity': 'ethereum_prices'}

class ethereum_news(currency_news, db.Model):
    __tablename__ = "ethereum_news"
    __mapper_args__ = {'polymorphic_identity': 'ethereum_news'}

db.create_all()
db.session.commit()


@app.route('/getinfo')
def get_info():
        currency = request.args.get('currency')
        print("Currency: " + currency)
        coin = currency_info.query.filter_by(name=currency).first()
        json_dict = {
                "name": coin.name,
                "symbol": coin.symbol,
                "logo": "",
                "description": coin.description,
                "last_updated": "",
                "date_added": coin.date_added,
                "website": coin.website,
                "technical_doc": ""
        }
        return json.dumps(json_dict)

@app.route('/getprice')
def get_price():
        currency = request.args.get('currency')
        print("Currency: " + currency)
        current_price = Prices(currency)
        return jsonify(current_price.get_price())

if __name__ == "__main__":
  app.run()

  