from datetime import datetime
import random
import sqlite3
import time 


def insert_weather_data(cursor, conn):
    now = datetime.now().isoformat()
    temperature: int = "{:.2f}".format(random.uniform(60.00, 90.00))
    humidity: int = "{:.2f}".format(random.uniform(30.00, 70.00))
    pressure:int = "{:.2f}".format(random.uniform(1000.00, 1025.00))

    cursor.execute("""
        INSERT INTO weather(timestamp, temperature, humidity, pressure)
        VALUES (?, ?, ?, ?)
    """, (now, temperature, humidity, pressure))

    conn.commit()
    print(f"Inserted: {now}, {temperature}°C, {humidity}%, {pressure} hPa")

def create_connection():
    conn = sqlite3.connect('instance/Data.db')
    return conn, conn.cursor()

def main():
    conn, cursor = create_connection()

    try:
        while True:
            insert_weather_data(cursor, conn)
            time.sleep(10)  # wait for 10 seconds
    except KeyboardInterrupt:
        print("\nSimulation stopped by user.")
    finally:
        conn.close()

if __name__ == "__main__":
    main()