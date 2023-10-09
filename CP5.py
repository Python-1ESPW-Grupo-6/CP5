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

# Função para adicionar tarefa
def adicionar_tarefa():
    global tarefas
    tarefa = {}
    tarefa['descricao'] = input("Descrição da tarefa: ")
    tarefa['data_inicial'] = input("Data inicial da tarefa (formato dd/mm/aaaa): ")
    tarefa['data_final'] = input("Data final da tarefa (formato dd/mm/aaaa): ")
    tarefa['completude_real'] = float(input("Percentual de completude real da tarefa: "))
    tarefa['completude_planejada'] = float(input("Percentual de completude planejada da tarefa: "))
    tarefa['responsavel'] = input("Responsável pela tarefa: ")
    tarefas.append(tarefa)
    print("Tarefa adicionada com sucesso.")

# Função para atualizar tarefa
def atualizar_tarefa():
    global tarefas
    print("Lista de tarefas:")
    listar_tarefas()
    num_tarefa = int(input("Digite o número da tarefa que deseja atualizar: ")) - 1
    if 0 <= num_tarefa < len(tarefas):
        tarefa = tarefas[num_tarefa]
        print("Atualize os campos (deixe em branco para manter os valores atuais):")
        tarefa['descricao'] = input(f"Nova descrição da tarefa ({tarefa['descricao']}): ") or tarefa['descricao']
        tarefa['data_inicial'] = input(f"Nova data inicial ({tarefa['data_inicial']}): ") or tarefa['data_inicial']
        tarefa['data_final'] = input(f"Nova data final ({tarefa['data_final']}): ") or tarefa['data_final']
        tarefa['completude_real'] = float(input(f"Novo percentual de completude real ({tarefa['completude_real']}): ")) or tarefa['completude_real']
        tarefa['completude_planejada'] = float(input(f"Novo percentual de completude planejada ({tarefa['completude_planejada']}): ")) or tarefa['completude_planejada']
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
        print(f"Completude real: {tarefa['completude_real']}%")
        print(f"Completude planejada: {tarefa['completude_planejada']}%")
        print(f"Responsável: {tarefa['responsavel']}")
        print("-----------------------------")

# Função para resumo da operação
def resumo_operacao():
    print("Resumo da operação:")
    listar_tarefas()

# Loop principal
while True:
    print("Opções:")
    print("1. Adicionar tarefa")
    print("2. Atualizar tarefa")
    print("3. Listar tarefas")
    print("4. Encerrar programa")
    escolha = input("Escolha uma opção: ")

    if escolha == '1':
        adicionar_tarefa()
    elif escolha == '2':
        atualizar_tarefa()
    elif escolha == '3':
        listar_tarefas()
    elif escolha == '4':
        break
    else:
        print("Opção inválida. Tente novamente.")

    resumo_operacao()
