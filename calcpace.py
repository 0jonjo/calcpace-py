dist = input('Qual a distância percorrida em km? Ex: X.X ')
tempo = input('Quanto tempo? Ex: HH:MM:SS?' )
hora, minuto, segundo = tempo.split(':')
h, m, s = 0, 0, 0

t = (int(hora)*60*60) + (int(minuto)*60) + int(segundo)
p = t / float(dist)
if p > 60:
    m += 1
else:
    s = p
    
print(f'Você percorreu os {dist}km no pace {m}:{s}.')
