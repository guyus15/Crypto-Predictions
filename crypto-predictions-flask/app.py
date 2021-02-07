from flask import Flask, request, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from prices import Prices
from news import News
import json
from datetime import datetime, timedelta
import time


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
    def __init__(self,last_updated,price,percent_change_1h,percent_change_24h,percent_change_7d):
        self.last_updated=last_updated
        self.price=price
        self.percent_change_1h=percent_change_1h
        self.percent_change_24h=percent_change_24h
        self.percent_change_7d=percent_change_7d

class bitcoin_news(currency_news, db.Model):
    __tablename__ = "bitcoin_news"
    __mapper_args__ = {'polymorphic_identity': 'bitcoin_news'}
    def __init__(self, uuid, last_updated, title, content, url, image_url, published):
        self.uuid=uuid
        self.last_updated=last_updated
        self.title=title
        self.content=content
        self.url=url
        self.image_url=image_url
        self.published=published

class ethereum_prices(currency_prices, db.Model):
    __tablename__ = "ethereum_prices"
    __mapper_args__ = {'polymorphic_identity': 'ethereum_prices'}
    def __init__(self,last_updated,price,percent_change_1h,percent_change_24h,percent_change_7d):
        self.last_updated=last_updated
        self.price=price
        self.percent_change_1h=percent_change_1h
        self.percent_change_24h=percent_change_24h
        self.percent_change_7d=percent_change_7d

class ethereum_news(currency_news, db.Model):
    __tablename__ = "ethereum_news"
    __mapper_args__ = {'polymorphic_identity': 'ethereum_news'}
    def __init__(self, uuid, last_updated, title, content, url, image_url, published):
        self.uuid=uuid
        self.last_updated=last_updated
        self.title=title
        self.content=content
        self.url=url
        self.image_url=image_url
        self.published=published

class dogecoin_prices(currency_prices, db.Model):
    __tablename__ = "dogecoin_prices"
    __mapper_args__ = {'polymorphic_identity': 'dogecoin_prices'}
    def __init__(self,last_updated,price,percent_change_1h,percent_change_24h,percent_change_7d):
        self.last_updated=last_updated
        self.price=price
        self.percent_change_1h=percent_change_1h
        self.percent_change_24h=percent_change_24h
        self.percent_change_7d=percent_change_7d

class dogecoin_news(currency_news, db.Model):
    __tablename__ = "dogecoin_news"
    __mapper_args__ = {'polymorphic_identity': 'dogecoin_news'}
    def __init__(self, uuid, last_updated, title, content, url, image_url, published):
        self.uuid=uuid
        self.last_updated=last_updated
        self.title=title
        self.content=content
        self.url=url
        self.image_url=image_url
        self.published=published

class litecoin_prices(currency_prices, db.Model):
    __tablename__ = "litecoin_prices"
    __mapper_args__ = {'polymorphic_identity': 'litecoin_prices'}
    def __init__(self,last_updated,price,percent_change_1h,percent_change_24h,percent_change_7d):
        self.last_updated=last_updated
        self.price=price
        self.percent_change_1h=percent_change_1h
        self.percent_change_24h=percent_change_24h
        self.percent_change_7d=percent_change_7d

class litecoin_news(currency_news, db.Model):
    __tablename__ = "litecoin_news"
    __mapper_args__ = {'polymorphic_identity': 'litecoin_news'}
    def __init__(self, uuid, last_updated, title, content, url, image_url, published):
        self.uuid=uuid
        self.last_updated=last_updated
        self.title=title
        self.content=content
        self.url=url
        self.image_url=image_url
        self.published=published

class binance_prices(currency_prices, db.Model):
    __tablename__ = "binance_prices"
    __mapper_args__ = {'polymorphic_identity': 'binance_prices'}
    def __init__(self,last_updated,price,percent_change_1h,percent_change_24h,percent_change_7d):
        self.last_updated=last_updated
        self.price=price
        self.percent_change_1h=percent_change_1h
        self.percent_change_24h=percent_change_24h
        self.percent_change_7d=percent_change_7d

class binance_news(currency_news, db.Model):
    __tablename__ = "binance_news"
    __mapper_args__ = {'polymorphic_identity': 'binance_news'}
    def __init__(self, uuid, last_updated, title, content, url, image_url, published):
        self.uuid=uuid
        self.last_updated=last_updated
        self.title=title
        self.content=content
        self.url=url
        self.image_url=image_url
        self.published=published

class bitcoin_cash_prices(currency_prices, db.Model):
    __tablename__ = "bitcoin_cash_prices"
    __mapper_args__ = {'polymorphic_identity': 'bitcoin_cash_prices'}
    def __init__(self,last_updated,price,percent_change_1h,percent_change_24h,percent_change_7d):
        self.last_updated=last_updated
        self.price=price
        self.percent_change_1h=percent_change_1h
        self.percent_change_24h=percent_change_24h
        self.percent_change_7d=percent_change_7d

class bitcoin_cash_news(currency_news, db.Model):
    __tablename__ = "bitcoin_cash_news"
    __mapper_args__ = {'polymorphic_identity': 'bitcoin_cash_news'}
    def __init__(self, uuid, last_updated, title, content, url, image_url, published):
        self.uuid=uuid
        self.last_updated=last_updated
        self.title=title
        self.content=content
        self.url=url
        self.image_url=image_url
        self.published=published

db_access_price = {"bitcoin":bitcoin_prices, "ethereum":ethereum_prices, "dogecoin":dogecoin_prices, "litecoin":litecoin_prices, "binance":binance_prices, "bitcoin_cash":bitcoin_cash_prices}
db_access_news = {"bitcoin":bitcoin_news, "ethereum":ethereum_news, "dogecoin":dogecoin_news, "litecoin":litecoin_news, "binance":binance_news, "bitcoin_cash":bitcoin_cash_news}


@app.route('/getinfo')
def get_info():
        currency = request.args.get('currency')
        currency = currency.capitalize()
        print("Currency: " + currency)
        if currency == "binance":
            coin = currency_info.query.filter_by(name="Binance Coin").first()
        elif currency == "bitcoin_cash":
            coin = currency_info.query.filter_by(name="Bitcoin Cash").first()
        else:
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
        values = db_access_price[currency].query.all()
        target_time=datetime.now()
        if len(values) != 0:
            time_comparison = values[-1].last_updated
            time_formatted = datetime.strptime(time_comparison,"%Y-%m-%dT%H:%M:%S.%fZ")
            if time_formatted+timedelta(minutes=1) > target_time:
                print("Time between calls too recent")
            else:
                if currency == "binance":
                    price = Prices("Binance Coin")
                elif currency == "bitcoin_cash":
                    price = Prices("Bitcoin Cash")
                else:
                    price = Prices(currency.capitalize())
                new_data = price.get_price()
                new_record = db_access_price[currency](new_data.get("last_updated"), new_data.get("quote").get("GBP").get("price"), new_data.get("quote").get("GBP").get("percent_change_1h"), new_data.get("quote").get("GBP").get("percent_change_24h"), new_data.get("quote").get("GBP").get("percent_change_7d"))
                db.session.add(new_record)
                db.session.commit()
        else:
            if currency == "binance":
                price = Prices("Binance Coin")
            elif currency == "bitcoin_cash":
                price = Prices("Bitcoin Cash")
            else:
                price = Prices(currency.capitalize())
            new_data = price.get_price()
            new_record = db_access_price[currency](new_data.get("last_updated"), new_data.get("quote").get("GBP").get("price"), new_data.get("quote").get("GBP").get("percent_change_1h"), new_data.get("quote").get("GBP").get("percent_change_24h"), new_data.get("quote").get("GBP").get("percent_change_7d"))
            db.session.add(new_record)
            db.session.commit()
        values = db_access_price[currency].query.all()
        json_dict = []
        last_updated, price, percent_change_1h, percent_change_24h, percent_change_7d = [], [], [], [], []
        for i in range(len(values)):
            last_updated.append(values[i].last_updated)
            price.append(values[i].price)
            percent_change_1h.append(values[i].percent_change_1h)
            percent_change_24h.append(values[i].percent_change_24h)
            percent_change_7d.append(values[i].percent_change_7d)
        for a, b, c, d, e in zip(last_updated, price, percent_change_1h, percent_change_24h, percent_change_7d):
            price_data = {"last_updated":a, "price":b, "percent_change_1h":c, "percent_change_24h":d, "percent_change_7d":e}
            json_dict.append(price_data)
        return json.dumps(json_dict)

@app.route('/getnews')
def get_news():
    currency = request.args.get('currency')
    stories = db_access_news[currency].query.all()
    target_time=datetime.now()
    if len(stories) != 0:
        time_comparison = stories[-1].last_updated
        time_formatted = datetime.strptime(time_comparison,"%Y-%m-%d %H:%M:%S.%f")
        if time_formatted+timedelta(minutes=1) > target_time:
            print("Time between calls too recent")
        else:
            news = News(currency)
            new_data = news.get_news()
            for i in range(len(new_data[0])):
                temp_story = db_access_news[currency].query.filter_by(uuid=new_data[0][i].get("uuid")).first()
                if temp_story == None:
                    new_record = db_access_news[currency](new_data[0][i].get("uuid"), datetime.now(), new_data[0][i].get("title"), new_data[0][i].get("snippet"), new_data[0][i].get("url"), new_data[0][i].get("image_url"), new_data[0][i].get("published_at"))
                    db.session.add(new_record)
            db.session.commit()
    else:
        news = News(currency)
        new_data = news.get_news()
        for i in range(len(new_data)):
            temp_story = db_access_news[currency].query.filter_by(uuid=new_data[0][i].get("uuid")).first()
            if temp_story == None:
                new_record = db_access_news[currency](new_data[0][i].get("uuid"), datetime.now(), new_data[0][i].get("title"), new_data[0][i].get("snippet"), new_data[0][i].get("url"), new_data[0][i].get("image_url"), new_data[0][i].get("published_at"))
                db.session.add(new_record)
        db.session.commit()
    stories = db_access_news[currency].query.all()
    json_dict = []
    uuid, last_updated, title, content, url, image_url, published_at = [], [], [], [], [], [], []
    for i in range(len(stories)):
        uuid.append(stories[i].uuid)
        last_updated.append(stories[i].last_updated)
        title.append(stories[i].title)
        content.append(stories[i].content)
        url.append(stories[i].url)
        image_url.append(stories[i].image_url)
        published_at.append(stories[i].published)
    for a, b, c, d, e, f, g in zip(uuid, last_updated, title, content, url, image_url, published_at):
        news_data = {"uuid":a, "last_updated":b, "title":c, "content":d, "url":e, "image_url":f,"published_at":g}
        json_dict.append(news_data)
    return json.dumps(json_dict)



if __name__ == "__main__":
  app.run()

  