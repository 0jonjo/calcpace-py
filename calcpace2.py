import time
from functions import dist
from functions import tempo
from functions import pace
from functions import prevcorrida
from functions import impressao

#Menu inicial
opcao = input('Escolha a opção desejada: \n [1. CALC PACE] [2. CALC TEMPO CORRIDA]\n [3. SALVAR CORRIDA] [4. VER/EDITAR CORRIDA]\n')
if opcao == '1':
    totaldistancia = dist()
    totaltempo = tempo()
    finalpace = pace(totaltempo, totaldistancia)
    impress = impressao(finalpace)
elif opcao == '2':
    totaldistancia = dist()
    totaltempo = tempo()
    calctempo = prevcorrida(totaltempo, totaldistancia)
    impress = impressao(calctempo)
elif opcao == '3':
    entradaData = input("Insira a data no formato DD/MM/AAAA: ")
    data = datetime.strptime(entradaData, "%d/%m/%Y")
else:
    print('')
