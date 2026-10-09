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

   opcoes = ["sim", "não", "nao"]

   while True:
       resposta_adicao = input("Você gostaria de adicionar uma tarefa à lista? Responda com 'Sim'ou 'Não'").lower()
       while resposta_adicao not in opcoes:
           resposta_adicao = input("Responda inválida! Responda somente com 'Sim' ou 'Não'").lower()
          
       while resposta_adicao == "sim":
           titulo_adicao = input("Qual o título da tarefa?")
           status_adicao = input("Qual o status da tarefa?")
           prioridade_adicao = input("Qual a prioridade da tarefa?")
      
       lista_de_nova_tarefa = [
       {"titulo": "titulo_adicao", "status": "status_adicao", "prioridade": "prioridade_adicao"}
       ]
       tarefas.append(lista_de_nova_tarefa)

def remover_tarefa():
  
   opcoes = ["sim", "não", "nao"]
  
   resposta_remocao = input("Você deseja remover uma tarefa da lista? (Sim/Não)").lower()
   while resposta_remocao not in opcoes:
       resposta_remocao = input("Responda inválida! Responda somente com 'Sim'ou 'Não'.").lower()

       while resposta_remocao == "sim":
           tarefa_deletada = ("Digite o nome da tarefa que você deseja deletar: ")
           for cada_item in tarefas:
               if cada_item['titulo'] == tarefa_deletada:
                   tarefas.remove(tarefa_deletada)

tarefas = [
   {"titulo": "Organizar a casa", "status": "Não concluído", "prioridade": "Alta"},
   {"titulo": "Ir para a escola/faculdade", "statu s": "Concluído", "prioridade": "Alta"},
   {"titulo": "Realizar as lições da escola/faculdade", "status": "Não concluído", "prioridade": "Média"},
   {"titulo": "Realizar exercícios práticos no violino", "status": "Concluído", "prioridade": "Média"},
   {"titulo": "Realizar a continuação da leitura do livro", "status": "Não concluído", "prioridade": "Baixa"},
   {"titulo": "Assistir um filme e realizar uma resenha técnica", "status": "Concluído", "prioridade": "Baixa"}
]
