"""
COMANDOS BÁSICOS EM PYTHON 7 - Funções
    Autor: Júlia Onora da Silva
    Data: 6 de janeiro de 2022
"""

def ola():
  print("Olá!")

ola()

for i in range(4):
  ola()

def ola2():
  return "Olá!"

print(ola2().upper())

def ola3(saudacao):
  return '{} funcao'.format(saudacao)

print(ola3("Oi"))

def ola4(saudacao, nome = "Você"):
  return '{} {} funcao'.format(saudacao,nome)

print(ola4("Oi"))

print(ola4("Oi", "Júlia"))

def estudante(*args, **kwargs):
  print(args)
  print(kwargs)

nome = "Júlia"
disciplina = {"prim": "Sistemas Dgitais", "segun": "Banco de Dados"}

estudante(*nome, **disciplina)

def ano_bisexto(mes):

  if mes == 29:
    print("Esse ano é ano bisexto.")
  
  else:
    print("Esse ano não é ano bisexto.")

fev = int(input("Qual a quantidade de dias do mês de fevereiro deste ano? "))

ano_bisexto(fev)
