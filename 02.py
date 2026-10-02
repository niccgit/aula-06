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
    resposta_nivel = input("Digite qual nível de prioridade das tarefas você deseja? (Alta/Média/Baixa)")
    for cada_item in tarefas:
        if cada_item["prioridade"] == resposta_nivel:
            print(f"Título: {cada_item['titulo']} | Status: {cada_item['status']} | Prioridade: {cada_item['prioridade']}")

def adicionar_nova_tarefa():
    
    opcoes = ["Sim", "Não", "Nao"]
    
    while True:
        resposta_adicao = input("Você gostaria de adicionar uma tarefa à lista? Responda com 'Sim'ou 'Não'").lower()
        while resposta_adicao not in opcoes:
            resposta_adicao = input("Responda inválida! Responda somente com 'Sim' ou 'Não'")
            
        while resposta_adicao == "sim":
            titulo_adicao = input("Qual o título da tarefa?")
            status_adicao = input("Qual o status da tarefa?")
            prioridade_adicao = input("Qual a prioridade da tarefa?")
        
    lista_de_nova_tarefa = [
        {"titulo": "titulo_adicao", "status": "status_adicao", "prioridade": "prioridade_adicao"}
    ]

    tarefas.append(lista_de_nova_tarefa)

tarefas = [
  {"titulo": "Organizar a casa", "status": "Não concluído", "prioridade": "Alta"},
  {"titulo": "Ir para a escola/faculdade", "statu s": "Concluído", "prioridade": "Alta"},
  {"titulo": "Realizar as lições da escola/faculdade", "status": "Não concluído", "prioridade": "Média"},
  {"titulo": "Realizar exercícios práticos no violino", "status": "Concluído", "prioridade": "Média"},
  {"titulo": "Realizar a continuação da leitura do livro", "status": "Não concluído", "prioridade": "Baixa"},
  {"titulo": "Assistir um filme e realizar uma resenha técnica", "status": "Concluído", "prioridade": "Baixa"}
]

while True:
    print("Organizador de tarefas")
    print("1 - Mostrar todas as tarefas")
    print("2 - Mostrar tarefas concluídas")
    print("3 - Mostrar tarefas não concluídas")
    print("4 - Mostrar tarefas por prioridades")
    print("5 - Cadastrar tarefa nova")
    print("6 - Finalizar tarefa")
    print("7 - Remover tarefa")
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
    elif opcao == "0":
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida. Tente novamente!")  
