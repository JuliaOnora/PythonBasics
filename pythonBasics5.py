"""
COMANDOS BÁSICOS EM PYTHON 5 - Operadores condicionais e lógica booleana
    Autor: Júlia Onora da Silva
    Data: 6 de janeiro de 2022
"""

variavel = "Python"

if variavel == "Python":
  print("Palavras iguais!")

else:
  print("Palavras diferentes")

variavel = "Java"

if variavel == "Python":
  print("Palavras iguais!")

elif variavel == "C++":
  print("Palavras iguais!")

elif variavel == "VBA":
  print("Palavras iguais!")

else:
  print("Palavras diferentes :(")

# Operador lógico and

user = "Adm"
status = "não logado"

if user == "Adm" and status == "logado":
  print("É possível fazer modificações")

else:
  print("Não possível fazer modificações")

# Operador lógico or

user = "Adm"
status = "não logado"

if user == "Adm" or status == "logado":
  print("É possível fazer modificações")

else:
  print("Não possível fazer modificações")

# Operador lógico not

user = "Adm"
status = False

if not status:
  print("É possível fazer modificações")

else:
  print("Não possível fazer modificações")

a = [1, 2]
b = [1, 2]
c = b

print(a == b) # True porque possuem os mesmo valores
print(a is b) # False porque não estão alocados no mesmo local da memória
print("ID de a: ", id(a))
print("ID de b: ", id(b))
print("ID de c: ", id(c))

# Avaliando palavra "None"

palavra = None

if palavra:
  print("Entendeu como verdade")

else:
  print("Entendeu como falso")



# Avaliando nro 0

palavra = 0

if palavra:
  print("Entendeu como verdade")

else:
  print("Entendeu como falso")

# Avaliando lista, string e tuplas vazias

palavra = ''
tupla = ()
lista = []

if palavra or tupla or lista:
  print("Entendeu como verdade")

else:
  print("Entendeu como falso")

# Avaliando dicionário vazio

palavra = {}

if palavra:
  print("Entendeu com verdade")

else:
  print("Entendeu como falso")

# Avaliando dicionário vazio

palavra = 'palavra'

if palavra:
  print("Entendeu com verdade")

else:
  print("Entendeu como falso")