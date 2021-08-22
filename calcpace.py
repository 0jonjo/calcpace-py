from functions import dist
from functions import timerun
from functions import adjust
from functions import calcpace
from functions import predictrun
from functions import converttime
from functions import toprint
from functions import date
from functions import observations
from functions import setdata
from functions import getdata
from functions import deletedata
from functions import createtable

#Menu inicial
print("""
CALCPACE
""")
option = input('Escolha a opção desejada:\n 1. CALCULAR O PACE\n 2. CALCULAR O TEMPO CORRIDA\n 3. SALVAR CORRIDA\n 4. DELETAR CORRIDA\n 5. VER CORRIDAS SALVAS\n Ctrl + C para sair do programa a qualquer momento\n')
if option == '1':
    total = dist()
    totaltime= timerun()
    adjusted = adjust(totaltime)
    finalpace = calcpace(adjusted, total)
    convertedpace = converttime(finalpace)
    impress = toprint(convertedpace)
elif option == '2':
    total = dist()
    totaltime= timerun()
    adjusted = adjust(totaltime)
    calctemp = predictrun(adjusted, total)
    convertedtemprun = converttime(calctemp)
    impress = toprint(convertedtemprun)
elif option == '3':
    createtable()
    thedate = date()
    total = dist()
    totaltime = timerun()
    adjusted = adjust(totaltime)
    finalpace = calcpace(adjusted, total)
    convertedpace = converttime(finalpace)           
    obs = observations()
    escrever = setdata(date, total, totaltime, convertedpace, obs)
elif option == '4':
    getdata()
    deletedata()
elif option == '5':
    getdata()
else:
    print('Opção inválida')
