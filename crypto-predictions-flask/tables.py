from flask_sqlalchemy import SQLAlchemy


class currency_prices(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    last_updated = db.Column(db.String(20))
    price = db.Column(db.Integer)
    percent_change_1h = db.Column(db.Integer)
    percent_change_24h = db.Column(db.Integer)
    percent_change_7d = db.Column(db.Integer)


class currency_news(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    last_updated = db.Column(db.String(20))
    title = db.Column(db.String(30))
    content = db.Column(db.String(2000))