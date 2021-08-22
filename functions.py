import time
import sqlite3

conn = sqlite3.connect("calpace.db")
curr = conn.cursor()

def dist():
    distance = input("Escreva a distância\n m = maratona, h = meia maratona ou digite os km em X.X ")
    if distance == 'm':
        d = 42.195
    elif distance == 'h':
        d = 21.0975
    else:
        d = distance
    return d


def timerun():
    temp = input("Escreva o tempo ou pace da corrida no formato HH:MM:SS) ")
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

def toprint(result):
    print(f'O resultado é {result}.')

def date():
    data = input("Insira a data no formato DD/MM/AAAA: ")
    return data

def observations():
    obs = input("Insira a observação: ")
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
        print("Tabela criada com sucesso")
    except:
        print("Já existe uma tabela")
    finally:
        conn.commit()

def setdata(data, dist, tempo, pace, obs):
         
    addData = f"""INSERT INTO DADOS VALUES('{data}', '{dist}', '{tempo}', '{pace}', '{obs}')"""
    print(addData)
    curr.execute(addData)
    print("Corrida salva com sucesso!")
    conn.commit()

def getdata():

    fetchData = "SELECT * from DADOS"
    curr.execute(fetchData)
    answer = curr.fetchall()
    for data in answer:
        print(data)

def deletedata():

    dataparadeletar = input("Escreva a data da corrida a ser deletada no formato DD/MM/AAAA: ")
    datadelete = f"""'{dataparadeletar}'"""
    deleteData = f"""DELETE FROM DADOS WHERE data={datadelete}"""
    curr.execute(deleteData)
    print("Corrida removida com sucesso!")
    conn.commit()
