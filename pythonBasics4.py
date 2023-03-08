"""
COMANDOS BÁSICOS EM PYTHON 4 - Dicionários
    Autor: Júlia Onora da Silva
    Data: 6 de janeiro de 2022
"""

dic1 = {"nome": "Júlia", "cursos": ["Sistemas Digitais", "Banco de Dados"]}

print(dic1)

print("Nome: ", dic1["nome"])
print("Cursos: ", dic1["cursos"])

# Imprimindo o nome de novo

print("Nome: ", dic1.get("nome"))

# Adicionando um valor ao dicionário, se a chave não existir, ou atualizar valaor se já existir

dic1['idade'] = 0
print("Novo dicionário: ", dic1)

dic1['idade'] = 1
print("Modificação: ", dic1)

# Atualizar um valor do dicionário

dic1.update({"nome": "Júlia Onora"})
print("Nova modificação: ", dic1)

# Excluir chave e valor

del dic1["idade"]
print("Nova modificação: ", dic1)

# Excluir chave e valor

dic2 = dic1.pop("cursos")
print("Novo dicionário: ", dic2)

# Imprimindo chaves e valores

print("Dicionário 1:" , dic1)
print("Quantidade de itens no dicionário 1: ", len(dic1))
print("Chaves do dicionário 1: ", dic1.keys())
print("Valores do dicionário 1: ", dic1.values())
print("Itens do dicionário 1: ", dic1.items())

for chave, valor in dic1.items():
  print("Chave: ", chave, " e valor: ", valor)