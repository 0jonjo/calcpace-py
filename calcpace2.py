from functions import dist
from functions import tempo
from functions import ajustetempo
from functions import pace
from functions import prevcorrida
from functions import convertertempo
from functions import impressao
from functions import entradadata
from functions import observacao
from functions import lerdados
from functions import escreverdados

#Menu inicial
opcao = input('Escolha a opção desejada: \n [1. CALC PACE] [2. CALC TEMPO CORRIDA]\n [3. SALVAR CORRIDA] [4. VER CORRIDAS SALVAS]\n')
if opcao == '1':
    totaldistancia = dist()
    totaltempo = tempo()
    ajuste = ajustetempo(totaltempo)
    finalpace = pace(ajuste, totaldistancia)
    converter = convertertempo(finalpace)
    impress = impressao(converter)
elif opcao == '2':
    totaldistancia = dist()
    totaltempo = tempo()
    ajuste = ajustetempo(totaltempo)
    calctempo = prevcorrida(totaltempo, totaldistancia)
    converter = convertertempo(finalpace)
    impress = impressao(converter)
elif opcao == '3':
    data = entradadata()
    totaldistancia = dist()
    totaltempo = tempo()
    ajuste = ajustetempo(totaltempo)
    finalpace = pace(ajuste, totaldistancia)
    converter = convertertempo(finalpace)           
    obs = observacao()
    escrever = escreverdados(str(data), totaldistancia, str(totaltempo), str(converter), obs)
elif opcao == '4':
    lerdados()
else:
    print('Opção inválida')
