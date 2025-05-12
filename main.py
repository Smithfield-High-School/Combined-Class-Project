from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///weatherData.db'
db = SQLAlchemy(app)

class weather(db.Model): #Change to Whatever name the table needs to be
     id = db.Column(db.Integer, primary_key = True)
     # Do the rest of your table data here


with app.app_context():
        db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)