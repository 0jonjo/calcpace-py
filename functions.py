import time
import datetime
from datetime import datetime
import csv
from csv import reader, writer

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
    entradaData = input("Insira a data no formato DD/MM/AAAA: ")
    data = datetime.strptime(entradaData, "%d/%m/%Y")
    return data

def observacao():
    obs = input("Insira a observação: ")
    return obs

def lerdados():
    with open('dadoscorrida.csv') as csv_file:
    
        csv_reader = csv.reader(csv_file, delimiter=',')

        for row in csv_reader:
            print(row)
            
def escreverdados(data, dist, tempo, pace, obs):
    with open('dadoscorrida.csv', 'a', newline='') as file:

        writer = csv.writer(file)
    
        writer.writerow([data, dist, tempo, pace, obs])
