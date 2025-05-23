from flask import Flask, render_template, url_for, request, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import sqlite3

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///Data.db'
db = SQLAlchemy(app)

class Weather(db.Model):
     # This is all the needed data for our weather table
     id = db.Column(db.Integer, primary_key = True)
     timestamp = db.Column(db.DateTime, default = datetime.now)
     temperature = db.Column(db.Integer, nullable = False)
     humidity = db.Column(db.Integer, nullable = False)
     pressure = db.Column(db.Integer, nullable = False)

class utility(db.Model): #this is the column do not delete!!!!
     id = db.Column(db.Integer, primary_key = True)
     timestamp = db.Column(db.DateTime, default= datetime.now, nullable = False)
     electricity_kwh = db.Column(db.Integer, nullable=False)
     water_gallons = db.Column(db.Integer, nullable=False)

with app.app_context():
        db.create_all()

@app.route('/', methods=['POST', 'GET'])
def index():
    conn = sqlite3.connect("instance/Data.db")
    cursor = conn.cursor()
    data = cursor.execute("SELECT id, electricity_kwh, water_gallons FROM utility").fetchall() 
    labels = [row[0] for row in data]
    edata = [row[1] for row in data]
    wdata = [row[2] for row in data]
    conn.close()


    return render_template('index.html',  edata=edata, wdata=wdata, labels=labels)

@app.route('/utilityHomepage', methods=['POST', 'GET'])
def utilityHomepage():
    if request.method == "POST" :
        inelect = int(request.form["Electricity"])
        inwater = int(request.form["Water"])
        indata = utility(electricity_kwh=inelect, water_gallons=inwater)

        try:
            db.session.add(indata)
            db.session.commit()
        except:
            print('Something Went Wrong adding to the DB')
        
        return redirect('/utilityHomepage')

    return render_template('utilityDash.html')

@app.route('/utilityExpand')
def utilityExpand():
    conn = sqlite3.connect("instance/Data.db")
    cursor = conn.cursor()
    data = cursor.execute("SELECT id, electricity_kwh, water_gallons FROM utility").fetchall() 
    labels = [row[0] for row in data]
    edata = [row[1] for row in data]
    wdata = [row[2] for row in data]
    conn.close() 
 
    return render_template("utilityExpand.html", edata=edata, wdata=wdata, labels=labels)


@app.route('/weatherHomepage', methods=['POST', 'GET'])
def weatherHomepage():
    if request.method == 'POST':
        weatherTemperature = int(request.form["temperature"])
        weatherHumidity = int(request.form["humidity"])
        weatherPressure = int(request.form["pressure"])
        newData = Weather(temperature = weatherTemperature, humidity = weatherHumidity,pressure = weatherPressure)
        try:
            db.session.add(newData)
            db.session.commit()
            return redirect('/weatherHomepage')
        except Exception as issue:
            return f'There was an issue adding that weather data: {issue}'
    else:
        weatherChanged = Weather.query.order_by(Weather.timestamp).all()
        return render_template('weather_dashboard.html', weatherChanged = weatherChanged)
    
@app.route('/weatherChartData')
def weatherChartData():
        conn = sqlite3.connect('instance/Data.db')
        cur = conn.cursor()
        cur.execute("SELECT temperature, humidity, pressure FROM weather")
        rows = cur.fetchall()
        conn.close()
        temps = []
        humidity = []
        pressure = []
        for row in rows:
            intemps = [row[0]]
            temps = temps + intemps
            inhumidity = [row[1]]
            humidity = humidity + inhumidity
            inPressure = [row[2]]
            pressure = pressure + inPressure
        data = [{'tempatures': temps, 'humidity': humidity, 'pressure': pressure}]
        return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)