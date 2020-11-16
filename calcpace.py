escolha = input("Digite 't' para prever um tempo de corrida\n ou qualquer tecla para calcular o pace: ")
h, m, s = 0, 0, 0

if escolha == 't':
    
    dist = float(input('Qual a distância a ser percorrida em km? Ex: X.X '))
    pace = input('Qual o pace desejado (M:S)? ' )
    minuto, segundo = pace.split(':')
    m = dist * int(minuto)
    s = dist * int(segundo)
    while s >= 60:
        m += 1
        s -= 60
    while m >= 60:
        h += 1
        m -= 60
    m, s = round(m), round(s)
    print(f'Você percorrerá os {dist}km no tempo de {h:0>2}h{m:0>2}min{s:0>2}seg.')

else:
    
    dist = input('Qual a distância percorrida em km? Ex: X.X ')
    tempo = input('Quanto tempo (H:M:S)? ' )
    hora, minuto, segundo = tempo.split(':')
    
    t = (int(hora)*3600) + (int(minuto)*60) + int(segundo)
    p = t / float(dist)
    while p >= 60:
        m += 1
        p -= 60
    p = round(p)
    print(f'Você percorreu os {dist}km no pace {m}:{p:0>2}.')
