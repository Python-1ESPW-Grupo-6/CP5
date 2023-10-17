'''
1ESPW

Fabrício Saavedra - 97631
Guilherme Akio - 98582
Guilherme Morais - 551981
Matheus Motta - 550352
Vinicius Buzato - 99125
'''

from datetime import datetime, date

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
    print('Valor inválido, por favor digite de acordo com o solicitado')

# Função para adicionar tarefa
def adicionar_tarefa():
    global tarefas
    tarefa = {}
    tarefa['descricao'] = input("Descrição da tarefa: ")

    while True:
        try:
            tarefa['data_inicial'] = datetime.strptime(input("Data inicial da tarefa (formato dd/mm/aaaa): "), "%d/%m/%Y").date()
            tarefa['data_inicial'] = tarefa['data_inicial'].strftime("%d/%m/%Y")
            break
        except ValueError:
            erro()
                                   
    while True:
        try:
            tarefa['data_final'] = datetime.strptime(input("Data final da tarefa (formato dd/mm/aaaa): "), "%d/%m/%Y").date()
            tarefa['data_final'] = tarefa['data_final'].strftime("%d/%m/%Y")
            if tarefa['data_final'] < tarefa['data_inicial']:
                print("A data final da nova tarefa não pode ser antes da data inicial, por favor revise sua tarefa")
            else:
                break
        except ValueError:
            erro()

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
    listar_tarefas()
    while True:
        try:
            num_tarefa = int(input("Digite o número da tarefa que deseja atualizar: ")) - 1
            paragrafo()
            if 0 <= num_tarefa < len(tarefas):
                tarefa = tarefas[num_tarefa]
                print("Atualize os campos (deixe em branco para manter os valores atuais):")

                tarefa['descricao'] = input("Nova descrição da tarefa: ") or tarefa['descricao']

                while True:
                    try:
                        nova_data_inicial = input("Nova data inicial (dd/mm/aaaa): ")
                        if nova_data_inicial != "":
                            tarefa['data_inicial'] = datetime.strptime(nova_data_inicial, "%d/%m/%Y").date()
                            tarefa['data_inicial'] = tarefa['data_inicial'].strftime("%d/%m/%Y")
                            break
                        else:
                            break
                    except ValueError:
                        erro()

                while True:
                    try:
                        nova_data_final = input("Nova data final (dd/mm/aaaa): ")
                        if nova_data_final != "":
                            tarefa['data_final'] = datetime.strptime(nova_data_final, "%d/%m/%Y").date()
                            tarefa['data_final'] = tarefa['data_final'].strftime("%d/%m/%Y")
                            if tarefa['data_final'] < tarefa['data_inicial']:
                                print("A data final da nova tarefa não pode ser antes da data inicial, por favor revise sua tarefa")
                            else:
                                break
                        else:
                            break
                    except ValueError:
                        erro()

                while True:
                    nova_complet_real = input("Novo percentual de completude real (apenas números): ")
                    if nova_complet_real == "":
                            break
                    try:
                        tarefa['completude_real'] = float(nova_complet_real)
                        break
                    except ValueError:
                        erro()

                while True:
                    nova_complet_plan = input("Novo percentual de completude planejada (apenas números): ")
                    if nova_complet_plan == "":
                            break
                    try:
                        tarefa['completude_planejada'] = float(nova_complet_plan)
                        break
                    except ValueError:
                        erro()
                                    
                tarefa['responsavel'] = input(f"Novo responsável ({tarefa['responsavel']}): ") or tarefa['responsavel']

                plano_atraso = input(f"Insira um  plano caso a tarefa esteja atrasada ou vá atrasar (deixei em branco caso não seja necessário): ")
                if plano_atraso != "":
                    tarefa['plano'] = plano_atraso

                    
                while True:
                    try:
                        conclusao_tarefa = input(f"Deseja marcar a tarefa como concluida? 'Sim' ou vazio para continuar: ").capitalize()
                        if conclusao_tarefa == "Sim":
                            tarefa['completude_real'] = tarefa['completude_planejada']
                            tarefa['concluida'] = conclusao_tarefa
                        break
                    except ValueError:
                        erro()

                print("Tarefa atualizada com sucesso.")

                break
            else:
                print("Número de tarefa inexistente.")
        except ValueError:
            erro()

# Função para listar tarefas
def listar_tarefas():
    print("[Lista de tarefas]")
    paragrafo()
    for i, tarefa in enumerate(tarefas, start=1):
        print(f"Tarefa {i}:")
        print(f"Descrição: {tarefa['descricao']}")
        print(f"Data inicial: {tarefa['data_inicial']}")
        print(f"Data final: {tarefa['data_final']}")
        print(f"Completude real: {tarefa['completude_real']:.0f}%")
        print(f"Completude planejada: {tarefa['completude_planejada']:.0f}%")
        print(f"Responsável: {tarefa['responsavel']}")
        data_final = datetime.strptime(tarefa['data_final'], '%d/%m/%Y')
        if data_final < datetime.now() and 'concluida' not in tarefa:
            print('Esta tarefa está atrasada!')
        if 'plano' in tarefa:
            print(f"Plano: {tarefa['plano']}")
        if 'concluida' in tarefa:
            print("Tarefa concluida")
        paragrafo()

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
            
    
