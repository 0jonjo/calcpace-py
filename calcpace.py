import time

escolha = input("Digite 't' para prever um tempo de corrida\n ou qualquer tecla para calcular o pace: ")

if escolha == 't':

    dist = input('Qual a distância a ser percorrida em km?\n m = maratona, h = meia maratona ou digite os km. Ex: X.X ')
    pace = input('Qual o pace desejado (M:S)? ')
    minuto, segundo = pace.split(':')
    t = int(minuto) * 60 + int(segundo)
    if dist == 'm':
        d = t * 42.195
    if dist == 'h':
        d = t * 21.0975
    else:
        d = float(dist) * t
    ty_res = time.gmtime(d)
    tempo_total = time.strftime("%H:%M:%S",ty_res)
    print(f'Você percorrerá a distância no tempo de {tempo_total}.')
    
else:

    dist = input('Qual a distância a ser percorrida em km?\n m = maratona, h = meia maratona ou digite os km. Ex: X.X ')
    tempo = input('Quanto tempo (H:M:S)? ')
    hora, minuto, segundo = tempo.split(':')
    t = (int(hora)*3600) + (int(minuto)*60) + int(segundo)
    if dist == 'm':
        p = t / 42.195
    if dist == 'h':
        p = t / 21.0975
    else:
        p = t / float(dist)
    ty_res = time.gmtime(p)
    pace = time.strftime("%M:%S",ty_res)
    print(f'Você percorreu a distância no pace {pace}.')
