import time

escolha = input("Digite 't' para prever um tempo de corrida\n ou qualquer tecla para calcular o pace: ")

if escolha == 't':

    dist = float(input('Qual a distância a ser percorrida em km? Ex: X.X '))
    pace = input('Qual o pace desejado (M:S)? ')
    minuto, segundo = pace.split(':')
    t = int(minuto) * 60 + int(segundo)
    d = dist * t
    ty_res = time.gmtime(d)
    tempo_total = time.strftime("%H:%M:%S",ty_res)
    print(f'Você percorrerá os {dist}km no tempo de {tempo_total}.')
    
else:

    dist = float(input('Qual a distância a ser percorrida em km? Ex: X.X '))
    tempo = input('Quanto tempo (H:M:S)? ')
    hora, minuto, segundo = tempo.split(':')
    t = (int(hora)*3600) + (int(minuto)*60) + int(segundo)
    p = t / dist
    ty_res = time.gmtime(p)
    pace = time.strftime("%M:%S",ty_res)
    print(f'Você percorreu os {dist}km no pace {pace}.')
