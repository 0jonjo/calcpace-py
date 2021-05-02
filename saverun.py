import time
import datetime
from datetime import datetime

entradaData = input("Insira a data no formato DD/MM/AAAA: ")
data = datetime.strptime(entradaData, "%d/%m/%Y")

distancia = input('Qual a distância percorrida em km?\n m = maratona, h = meia maratona ou digite os km. Ex: X.X ')

def dist(distancia):
    if distancia == 'm':
        c = 42.195
    elif distancia == 'h':
        c = 21.0975
    else:
        c = distancia
    return c

totaldistancia = dist(distancia)

temp = input('Escreva o tempo da corrida formato (H:M:S)? ')

def tempo(temp):
    hora, minuto, segundo = temp.split(':')
    t = (int(hora)*3600) + (int(minuto)*60) + int(segundo)
    return t

totaltempo = tempo(temp)

def pace(pacetempo, pacedistancia):
    p = float(pacetempo) / float(pacedistancia)
    ty_res = time.gmtime(p)
    resultadopace = time.strftime("%H:%M:%S",ty_res)
    return resultadopace

finalpace = pace(totaltempo, totaldistancia)

def prevcorrida(pacetempo, distancia):
    p = float(pacetempo) * float(distancia)
    ty_res = time.gmtime(p)
    resultadotempocorrida = time.strftime("%H:%M:%S",ty_res)
    return resultadotempocorrida

