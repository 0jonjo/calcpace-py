import time

#Escolha da distância base para os cálculos
dist = input('Qual a distância a ser percorrida em km?\n m = maratona, h = meia maratona ou digite os km. Ex: X.X ')
if dist == 'm':
    c = 42.195
if dist == 'h':
    c = 21.0975
else:
    c = float(dist)
    
#Input do tempo total de prova ou do pace
tempo = input('Quanto tempo ou pace. Escreva no formato (H:M:S)? ')
hora, minuto, segundo = tempo.split(':')
t = (int(hora)*3600) + (int(minuto)*60) + int(segundo)

#Escolha da opção de calculo - 0 para tempo de corrida / qualquer tecla para pace    
escolha = input("Digite '0' para prever um tempo de corrida\n ou qualquer tecla para calcular o pace: ")
if escolha == '0':
    d = t * c
else:
    d = t / c
    
#Padronização de formato e impressão do resultado de acordo com a escolha do usuário
ty_res = time.gmtime(d)
resultado = time.strftime("%H:%M:%S",ty_res)
print(f'Você percorrerá em {resultado}.')
    
