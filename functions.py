import time
import datetime
from datetime import datetime

def dist():
    distancia = input('Qual a distância percorrida em km?\n m = maratona, h = meia maratona ou digite os km. Ex: X.X ')
    if distancia == 'm':
        d = 42.195
    elif distancia == 'h':
        d = 21.0975
    else:
        d = distancia
    return d

def tempo():
    temp = input('Escreva o tempo ou pace da corrida formato (H:M:S)? ')
    hora, minuto, segundo = temp.split(':')
    t = (int(hora)*3600) + (int(minuto)*60) + int(segundo)
    return t

def pace(pacetempo, pacedistancia):
    resultadopace = float(pacetempo) / float(pacedistancia)
    return resultadopace

def prevcorrida(pacetempo, distancia):
    resultadotempocorrida = float(pacetempo) * float(distancia)
    return resultadotempocorrida

def impressao(d):
    ty_res = time.gmtime(d)
    resultado = time.strftime("%H:%M:%S",ty_res)
    print(f'O resultado é {resultado}.')

