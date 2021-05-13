from functions import dist
from functions import tempo
from functions import ajustetempo
from functions import pace
from functions import prevcorrida
from functions import convertertempo
from functions import impressao
from functions import entradadata
from functions import observacao
from functions import inserirdados
from functions import verdados
from functions import deletardados
from functions import criartabela

#Menu inicial
opcao = input('Escolha a opção desejada:\n [1. CALC PACE] [2. CALC TEMPO CORRIDA]\n [3. SALVAR CORRIDA] [4. VER CORRIDAS SALVAS]\n [5. DELETAR CORRIDA]\n')
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
    criartabela()
    data = entradadata()
    totaldistancia = dist()
    totaltempo = tempo()
    ajuste = ajustetempo(totaltempo)
    finalpace = pace(ajuste, totaldistancia)
    converter = convertertempo(finalpace)           
    obs = observacao()
    escrever = inserirdados(data, totaldistancia, totaltempo, converter, obs)
elif opcao == '4':
    verdados()
elif opcao == '5':
    verdados()
    deletardados()
else:
    print('Opção inválida')
