from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# make sure config file is in the same dir as this application.py
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://fuyxykyn:ZAHgMBMPA3sDkYWaGR0l2I-UP8Aq4pMX@drona.db.elephantsql.com:5432/fuyxykyn'
# it will rely on psycopg2 as well, should be installed
# psycopg2-binary should be installed as well

db = SQLAlchemy(app)


class Test(db.Model):
    id = db.Column(db.Integer, primary_key=True)


if __name__ == '__main__':
    app.run(debug=True)
