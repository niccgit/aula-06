clientes = [    
    {"nome": "Ana", "cel": "123", "empresa": "FIAT"},
    {"nome": "Pedro", "cel": "123", "empresa": "INTEL"},
    {"nome": "Maria", "cel": "123", "empresa": "SEBRAE"},
    {"nome": "Felipe", "cel": "123", "empresa": "INTEL"}
]

tipo_empresa = input("Digite qual empresa você gostaria de saber os clientes: ")
for cliente in clientes:
    if cliente["empresa"] == "tipo_empresa":
        print(clientes) 

#adicionar um cliente 
        
novo_nome = input("Digite o nome do cliente: ")
novo_cel = int(input("Digite o número de celular do cliente: "))
nova_empresa = input("Digite o nome da empresa do cliente: ")

clientes = {
    "nome": novo_nome,
    "cel": novo_cel,
    "empresa": nova_empresa
}
clientes.append(novo_nome)
print(clientes)

#remover um cliente

deletar = input("Digite o nome do cliente que você deseja deletar: ")
for cliente in clientes:
    if cliente["nome"] == "deletar":
        clientes.remove(deletar)
        break

print(clientes)