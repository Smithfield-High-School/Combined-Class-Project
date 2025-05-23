import sqlite3
import random
import time
from datetime import datetime

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