from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///Data.db'
db = SQLAlchemy(app)

class weather(db.Model):
     # This is all the needed data for our weather table
     id = db.Column(db.Integer, primary_key = True)
     timestamp = db.Column(db.DateTime, default = datetime.now().isoformat())
     temperature = db.Column(db.Integer, nullable = False)
     humidity = db.Column(db.Integer, nullable = False)
     pressure = db.Column(db.Integer, nullable = False)

class utility(db.Model):
     id = db.Column(db.Integer, primary_key = True)
     timestamp = db.Column(db.DateTime, default = datetime.now().isoformat())
     electricity_kwh = db.Column(db.Integer, nullable = False)
     water_gallons = db.Column(db.Integer, nullable = False)

with app.app_context():
        db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)