def menu_text():
    print("""
         CALCPACE
               """)
    print ("""Escolha a opção desejada:
    1. CALCULAR O PACE 
    2. CALCULAR O TEMPO CORRIDA
    3. SALVAR CORRIDA
    4. DELETAR CORRIDA
    5. VER CORRIDAS SALVAS
    Ctrl + C para sair do programa a qualquer momento""")

def dist_text():
    print("Escreva a distância\n m = maratona, h = meia maratona ou digite os km em X.X ")

def timerun_text():
    print("Escreva o tempo ou pace da corrida no formato HH:MM:SS")

def toprint(result):
    print(f'O resultado é {result}.')

def date_text():
    print("Insira a data no formato DD/MM/AAAA: ")

def observations_text():
    print("Insira a observação: ")

def runsaved_text():
    print("Corrida salva com sucesso!")

def rundeleted_text():
    print("Corrida removida com sucesso!")

def tablecreated_text():
    print("Tabela criada com sucesso")

def tabledeleted_text():
    print("Já existe uma tabela")

def datedelete_text():
    print("Escreva a data da corrida a ser deletada no formato DD/MM/AAAA: ")

def invalidoption_text():
    print('Opção inválida')