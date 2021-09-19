import time
import sqlite3
from texts import datedelete_text, dist_text
from texts import timerun_text
from texts import toprint
from texts import date_text
from texts import observations_text
from texts import runsaved_text
from texts import rundeleted_text
from texts import tablecreated_text
from texts import tabledeleted_text
from texts import datedelete_text

conn = sqlite3.connect("calpace.db")
curr = conn.cursor()

def dist():
    dist_text()
    distance = input()
    if distance == 'm':
        d = 42.195
    elif distance == 'h':
        d = 21.0975
    else:
        d = distance
    return d

def timerun():
    timerun_text()
    temp = input()
    return temp
    
def adjust(timerun):
    hour, minute, seconds = timerun.split(':')
    adjustedtime = (int(hour)*3600) + (int(minute)*60) + int(seconds)
    return adjustedtime

def calcpace(pacetime, pacedistance):
    resultpace = float(pacetime) / float(pacedistance)
    return resultpace

def predictrun(pacetime, distance):
    predict = float(pacetime) * float(distance)
    return predict

def converttime(t):
    ty_res = time.gmtime(t)
    result = time.strftime("%H:%M:%S",ty_res)
    return result

def date():
    date_text()
    data = input()
    return str(data)

def observations():
    observations_text()
    obs = input()
    return obs

def createtable():

    createTableCommand =  """CREATE TABLE DADOS (
    data TEXT PRIMARY KEY,
    distancia REAL NOT NULL,
    tempo TEXT NOT NULL,
    pace TEXT NOT NULL,
    obs TEXT
    );"""

    try: 
        curr.execute(createTableCommand)
        tablecreated_text()
    except:
        tabledeleted_text()
    finally:
        conn.commit()

def setdata(data, dist, tempo, pace, obs):
         
    addData = f"""INSERT INTO DADOS VALUES('{data}', '{dist}', '{tempo}', '{pace}', '{obs}')"""
    print(addData)
    curr.execute(addData)
    runsaved_text
    conn.commit()

def getdata():

    fetchData = "SELECT * from DADOS"
    curr.execute(fetchData)
    answer = curr.fetchall()
    for data in answer:
        print(data)

def deletedata():

    datedelete_text()
    dataparadeletar = input()
    datadelete = f"""'{dataparadeletar}'"""
    deleteData = f"""DELETE FROM DADOS WHERE data={datadelete}"""
    curr.execute(deleteData)
    rundeleted_text()
    conn.commit()
