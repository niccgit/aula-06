tarefas = [
    {'titulo': "Organizar a casa", 'status': "Não concluído", 'prioridade': "Alta"},
    {'titulo': "Ir para a escola/faculdade", 'status': "Concluído", 'prioridade': "Alta"},
    {'titulo': "Realizar as lições da escola/faculdade", 'status': "Não concluído", 'prioridade': "Média"},
    {'titulo': "Realizar exercícios práticos no violino", 'status': "Concluído", 'prioridade': "Média"},
    {'titulo': "Realizar a continuação da leitura do livro", 'status': "Não concluído", 'prioridade': "Baixa"},
    {'titulo': "Assistir um filme e realizar uma resenha técnica", 'status': "Concluído", 'prioridade': "Baixa"}
]

def mostrar_todas_tarefas():
    for cada_item in tarefas:
        print(f"Título: {cada_item['titulo']} | Status: {cada_item['status']} | Prioridade: {cada_item['prioridade']}")

def mostrar_concluidas():
    for cada_item in tarefas:
        if cada_item["status"] == "Concluído":
            print(f"Título: {cada_item['titulo']} | Status: {cada_item['status']} | Prioridade: {cada_item['prioridade']}")

def mostrar_nao_concluidas():
    for cada_item in tarefas:
        if cada_item["status"] == "Não concluído":
            print(f"Título: {cada_item['titulo']} | Status: {cada_item['status']} | Prioridade: {cada_item['prioridade']}")

def mostrar_por_prioridades():
    resposta_nivel = input("Digite qual nível de prioridade das tarefas você deseja? (Alta/Média/Baixa) ")
    for cada_item in tarefas:
        if cada_item["prioridade"] == resposta_nivel:
            print(f"Título: {cada_item['titulo']} | Status: {cada_item['status']} | Prioridade: {cada_item['prioridade']}")

def adicionar_nova_tarefa():
    
    opcoes = ["sim", "não", "nao"]

    resposta_adicao = input("Você gostaria de adicionar uma tarefa à lista? (Sim/Não) ").lower()
    while resposta_adicao not in opcoes:
        resposta_adicao = input("Resposta inválida! Responda somente com 'Sim' ou 'Não': ").lower()

    while resposta_adicao == "sim":
        titulo_adicao = input("Qual o título da nova tarefa? ")
        status_adicao = input("Qual o status da nova tarefa? (Concluído/Não concluído) ")
        prioridade_adicao = input("Qual a prioridade da nova tarefa? (Alta/Média/Baixa) ")

        nova_tarefa = {
            'titulo': titulo_adicao,
            'status': status_adicao,
            'prioridade': prioridade_adicao
        }
        tarefas.append(nova_tarefa)
        print("Tarefa adicionada com sucesso!")

        resposta_adicao = input("Deseja adicionar outra tarefa? (Sim/Não) ").lower()
        while resposta_adicao not in opcoes:
            resposta_adicao = input("Resposta inválida! Responda somente com 'Sim' ou 'Não': ").lower()

def remover_tarefa():
    
    opcoes = ["sim", "não", "nao"]

    resposta_remocao = input("Você gostaria de remover uma tarefa da lista? (Sim/Não) ").lower()
    while resposta_remocao not in opcoes:
        resposta_remocao = input("Resposta inválida! Responda somente com 'Sim' ou 'Não': ").lower()

    while resposta_remocao == "sim":
        tarefa_del = input("Digite o título da tarefa que você deseja remover: ")

        for cada_item in tarefas:
            if cada_item['titulo'] == tarefa_del:
                tarefas.remove(cada_item)
                print("Tarefa removida com sucesso!")
                break
        else:
            print("Tarefa não encontrada.")

        resposta_remocao = input("Deseja remover outra tarefa? (Sim/Não) ").lower()
        while resposta_remocao not in opcoes:
            resposta_remocao = input("Resposta inválida! Responda somente com 'Sim' ou 'Não': ").lower()

while True:
    print("\nLista de Tarefas")
    print("1 - Mostrar todas as tarefas")
    print("2 - Mostrar tarefas concluídas")
    print("3 - Mostrar tarefas não concluídas")
    print("4 - Mostrar tarefas por prioridade")
    print("5 - Adicionar nova tarefa")
    print("6 - Remover tarefa")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        mostrar_todas_tarefas()
    elif opcao == "2":
        mostrar_concluidas()
    elif opcao == "3":
        mostrar_nao_concluidas()
    elif opcao == "4":
        mostrar_por_prioridades()
    elif opcao == "5":
        adicionar_nova_tarefa()
    elif opcao == "6":
        remover_tarefa()
    elif opcao == "0":
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida. Tente novamente!")
