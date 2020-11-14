dist = input('Qual a distância percorrida em km? Ex: X.X ')
tempo = input('Quanto tempo (H:M:S)? ' )
hora, minuto, segundo = tempo.split(':')
m, s = 0, 0

t = (int(hora)*60*60) + (int(minuto)*60) + int(segundo)
p = t / float(dist)
while p >= 60:
    m += 1
    p = p - 60
p = round(p)
print(f'Você percorreu os {dist}km no pace {m}:{p}.')
