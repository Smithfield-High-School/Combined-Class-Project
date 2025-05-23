from random import randrange
import time
import sqlite3

data_set = 40
data_set2 = 40
con = sqlite3.connect("instance/Data.db")
cur = con.cursor()
# cur.execute(f"DELETE FROM utility WHERE id>0")


def limit60(num):
    if num > 60:
        num = 60
    elif num < 20:
        num = 20
    return(num)

while True:
    
    data_set += randrange(-6, 6)
    data_set2 += randrange(-6, 6)
    data_set = limit60(data_set)
    data_set2 = limit60(data_set2)
    
    cur.execute(f"""INSERT INTO utility (timestamp, electricity_kwh, water_gallons) VALUES(?,?,?)""", (time.ctime(),data_set,data_set2))
    con.commit()
    print("runnning!")
    time.sleep(10)