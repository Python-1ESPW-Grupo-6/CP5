'''
1ESPW

Fabrício Saavedra - 97631
Guilherme Akio - 98582
Guilherme Morais - 551981
Matheus Motta - 550352
Vinicius Buzato - 99125
'''

# Inicializar estruturas de dados para armazenar as tarefas
tarefas = []

#Função para imprimir o a marca da vinheria agnello
def logo():
    print("")
    print("''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''")                                                 
    print(' _____ _     _           _        _____             _ _       ')
    print('|  |  |_|___| |_ ___ ___|_|___   |  _  |___ ___ ___| | |___   ')
    print("|  |  | |   |   | -_|  _| | .'|  |     | . |   | -_| | | . |  ")
    print(" \___/|_|_|_|_|_|___|_| |_|__,|  |__|__|_  |_|_|___|_|_|___|  ")
    print("                                       |___|                  ")   
    print("''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''")

#Função para espaçamento entre retornos do código
def paragrafo():
    print("")

#Função para valor inválido
def erro():
    print('Valor inválido, por favor digite um valor válido')

# Função para adicionar tarefa
def adicionar_tarefa():
    global tarefas
    tarefa = {}
    tarefa['descricao'] = input("Descrição da tarefa: ")
    tarefa['data_inicial'] = input("Data inicial da tarefa (formato dd/mm/aaaa): ")
    tarefa['data_final'] = input("Data final da tarefa (formato dd/mm/aaaa): ")
    while True:
        try:
            tarefa['completude_real'] = float(input("Percentual de completude real da tarefa: "))
            break
        except ValueError: 
            erro()
    while True:
        try:
            tarefa['completude_planejada'] = float(input("Percentual de completude planejada da tarefa: "))
            break
        except ValueError:
            erro()
    tarefa['responsavel'] = input("Responsável pela tarefa: ")
    tarefas.append(tarefa)
    print("Tarefa adicionada com sucesso.")

# Função para atualizar tarefa
def atualizar_tarefa():
    global tarefas
    print("Lista de tarefas:")
    listar_tarefas()
    num_tarefa = int(input("Digite o número da tarefa que deseja atualizar: ")) - 1
    paragrafo()
    if 0 <= num_tarefa < len(tarefas):
        tarefa = tarefas[num_tarefa]
        print("Atualize os campos (deixe em branco para manter os valores atuais):")
        tarefa['descricao'] = input(f"Nova descrição da tarefa ({tarefa['descricao']}): ") or tarefa['descricao']
        tarefa['data_inicial'] = input(f"Nova data inicial ({tarefa['data_inicial']}): ") or tarefa['data_inicial']
        tarefa['data_final'] = input(f"Nova data final ({tarefa['data_final']}): ") or tarefa['data_final']
        while True:
            try:
                tarefa['completude_real'] = float(input(f"Novo percentual de completude real ({tarefa['completude_real']}): ")) or tarefa['completude_real']
                break
            except ValueError:
                erro()
        while True:
            try:
                tarefa['completude_planejada'] = float(input(f"Novo percentual de completude planejada ({tarefa['completude_planejada']}): ")) or tarefa['completude_planejada']
                break
            except ValueError:
                erro()
        tarefa['responsavel'] = input(f"Novo responsável ({tarefa['responsavel']}): ") or tarefa['responsavel']
        print("Tarefa atualizada com sucesso.")
    else:
        print("Número de tarefa inválido.")

# Função para listar tarefas
def listar_tarefas():
    for i, tarefa in enumerate(tarefas, start=1):
        print(f"Tarefa {i}:")
        print(f"Descrição: {tarefa['descricao']}")
        print(f"Data inicial: {tarefa['data_inicial']}")
        print(f"Data final: {tarefa['data_final']}")
        print(f"Completude real: {tarefa['completude_real']:.0f}%")
        print(f"Completude planejada: {tarefa['completude_planejada']}%")
        print(f"Responsável: {tarefa['responsavel']}")

# Função para resumo da operação
def resumo_operacao():
    print("Resumo da operação:")
    if len(tarefas) == 0:
        print("Nenhuma tarefa realizada")
    else:
        listar_tarefas()

# Loop principal
logo()

print("Bem vindo ao gerenciador de tarefas de vinheria Agnello.")

while True:
    escolha = input('''\n O que você deseja fazer hoje?:
    [1] Adicionar tarefa
    [2] Atualizar tarefa
    [3] Listar tarefas
    [4] Encerrar programa\nEscolha uma opção: ''')
    paragrafo()

    match escolha:
        case "1":
            adicionar_tarefa()
        case "2":
            atualizar_tarefa()
        case "3":
            listar_tarefas()
        case "4":
            resumo_operacao()
            break
        case _:
            erro()
            
    
