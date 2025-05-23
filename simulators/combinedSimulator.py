import sqlite3
import random
import time
from datetime import datetime
from random import randrange

# cur.execute(f"DELETE FROM utility WHERE id>0")


# Team A:

def teamASim():
    def create_connection():
        conn = sqlite3.connect('instance/Data.db')
        return conn, conn.cursor()
    
    def insert_weather_data(cursor, conn):
        now = datetime.now().isoformat()
        temperature = round(random.gauss(20, 3), 1)
        humidity = random.randint(40, 100)
        pressure = round(random.gauss(1013, 5), 1)

        cursor.execute("""
            INSERT INTO weather (timestamp, temperature, humidity, pressure)
            VALUES (?, ?, ?, ?)
        """, (now, temperature, humidity, pressure))

        conn.commit()
        print(f"Inserted: {now}, {temperature}°C, {humidity}%, {pressure} hPa")

    
    conn, cursor = create_connection()
    try:
        insert_weather_data(cursor, conn)
    except KeyboardInterrupt:
        print("\nSimulation stopped by user.")
    finally:
        conn.close()

# Team B:

def teamBSim():
    data_set = 40
    data_set2 = 40
    con = sqlite3.connect("instance/Data.db")
    cur = con.cursor()
    
    def limit60(num):
        if num > 60:
            num = 60
        elif num < 20:
            num = 20
        return(num)

        
    data_set += randrange(-6, 6)
    data_set2 += randrange(-6, 6)
    data_set = limit60(data_set)
    data_set2 = limit60(data_set2)
        
    cur.execute(f"""INSERT INTO utility (timestamp, electricity_kwh, water_gallons) VALUES(?,?,?)""", (time.ctime(),data_set,data_set2))
    con.commit()
    print("runnning!")


while True:
    teamASim()
    teamBSim()
    time.sleep(10)