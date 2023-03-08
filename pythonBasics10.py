"""
COMANDOS BÁSICOS EM PYTHON 10 - Arquivos
    Autor: Júlia Onora da Silva
    Data: 6 de janeiro de 2022
"""

# Abrir arquivo e ler
f = open("./teste.txt", 'r')

print(f.name)

f.close()


# Abrir arquivo e ler e então fechar
with open("teste.txt", 'r') as f:
    pass

print(f.mode)
print(f.closed) # arquivo fechado

with open('teste.txt', 'r') as f:
  conteudo = f.read()
  print(conteudo)

with open('teste.txt', 'r') as f:
  conteudo = f.readlines()
  print(conteudo)

with open('teste.txt', 'r') as f:
  conteudo = f.readline()
  print(conteudo)

with open('teste.txt', 'r') as f:
  for line in f:
    print(line, end='')


# Imprimindo os 10 primeiros caracteres
with open('teste.txt', 'r') as f:
  conteudo = f.read(10)
  print(conteudo, end='')


# Criando um arquivo
with open('teste2.txt', 'w') as f:
    f.write('TESTE.txt')
