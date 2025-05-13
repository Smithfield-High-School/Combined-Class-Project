from datetime import datetime
import random
import sqlite3
import time 


def insert_weather_data(cursor, conn):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    temperature = round(random.gauss(20, 3), 2)
    humidity = round(random.randint(30, 70), 2)
    pressure = round(random.gauss(1013, 5), 2)

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