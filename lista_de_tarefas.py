# Faça uma lista de tarefas em Python
# 
# 1 - Mostrar todas as tarefas
# 2 - Mostrar tarefas concluídas
# 3 - Mostrar tarefas não concluídas
# 4 - Mostrar tarefas por prioridades
# 5 - Cadastrar tarefa nova
# 6 - Finalizar tarefa
# 7 - Remover tarefa
# 0 - Sair

def mostrar_todas_tarefas():
   for cada_item in tarefas:
      print(f"Título: {cada_item['titulo']} | Status: {cada_item['status']} | Prioridade: {cada_item['prioridade']}")


tarefas = [
   {"Título": "Organizar a casa", "Status": "Não concluído", "Prioridade": "Alta"},
   {"Título": "Ir para a escola/faculdade", "Status": "Concluído", "Prioridade": "Alta"},
   {"Título": "Realizar as lições da escola/faculdade", "Status": "Não concluído", "Prioridade": "Média"},
   {"Título": "Realizar exercícios práticos no violino", "Status": "Concluído", "Prioridade": "Média"},
   {"Título": "Realizar a continuação da leitura do livro", "Status": "Não concluído", "Prioridade": "Baixa"},
   {"Título": "Assistir um filme e realizar uma resenha técnica", "Status": "Concluído"}
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
   else:
      print("Opção inválida. Tente novamente!")