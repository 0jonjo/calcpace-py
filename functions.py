import time
import datetime
from datetime import datetime
import csv
from csv import reader, writer
import sqlite3

conn = sqlite3.connect("calpace.db")
curr = conn.cursor()

def dist():
    distancia = input("Escreva a distância em km?\n m = maratona, h = meia maratona ou digite os km em X.X ")
    if distancia == 'm':
        d = 42.195
    elif distancia == 'h':
        d = 21.0975
    else:
        d = distancia
    return d

def tempo():
    temp = input("Escreva o tempo ou pace da corrida formato HH:MM:SS) ")
    return temp
    
def ajustetempo(temp):
    hora, minuto, segundo = temp.split(':')
    t = (int(hora)*3600) + (int(minuto)*60) + int(segundo)
    return t

def pace(pacetempo, pacedistancia):
    resultadopace = float(pacetempo) / float(pacedistancia)
    return resultadopace

def prevcorrida(pacetempo, distancia):
    resultadotempocorrida = float(pacetempo) * float(distancia)
    return resultadotempocorrida

def convertertempo(t):
    ty_res = time.gmtime(t)
    resultado = time.strftime("%H:%M:%S",ty_res)
    return resultado

def impressao(i):
    print(f'O resultado é {i}.')

def entradadata():
    data = input("Insira a data no formato DD/MM/AAAA: ")
    return data

def observacao():
    obs = input("Insira a observação: ")
    return obs

def criartabela():

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

def inserirdados(data, dist, tempo, pace, obs):
         
    addData = f"""INSERT INTO DADOS VALUES('{data}', '{dist}', '{tempo}', '{pace}', '{obs}')"""
    print(addData)
    curr.execute(addData)
    print("Corrida salva com sucesso!")
 
    conn.commit()

def verdados():

    fetchData = "SELECT * from DADOS"
 
    curr.execute(fetchData)
 
    answer = curr.fetchall()
 
    for data in answer:
        print(data)

def deletardados():

    dataparadeletar = input("Escreva a data da corrida a ser deletada no formato DD/MM/AAAA: ")
    datadelete = f"""'{dataparadeletar}'"""
    deleteData = f"""DELETE FROM DADOS WHERE data={datadelete}"""
    curr.execute(deleteData)
    print("Corrida removida com sucesso!")

    conn.commit()
