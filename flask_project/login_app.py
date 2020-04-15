from flask import Flask
from flask_login import LoginManager, UserMixin
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SECRET_KEY'] = 'Thisissecret!'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'postgres://fuyxykyn:ZAHgMBMPA3sDkYWaGR0l2I-UP8Aq4pMX@drona.db.elephantsql.com:5432/fuyxykyn'

login_manager = LoginManager(app)
db = SQLAlchemy(app)


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True)


if __name__ == '__main__':
    app.run(debug=True)