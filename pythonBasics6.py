"""
COMANDOS BÁSICOS EM PYTHON 6 - Estruturas de repetição
    Autor: Júlia Onora da Silva
    Data: 6 de janeiro de 2022
"""

nros = [1, 2, 3, 4]

for num in nros:
  print(num)

for num in nros:
  if num == 3:
    print(num)
    print("Nro 3 encontrado!")
    break # Responsável por sair do loop for
  print(num)

for num in nros:
  if num == 3:
    print(num)
    print("Nro 3 encontrado!")
    continue # Responsável por ir para apróxima interação
  print(num)

nros = [1, 2, 3, 4]
letras = ['a', 'b', 'c', 'd']

for num in nros:
  for letter in letras:
    print(num, letter)

for i in range(1, 10):
  print(i)

x = 0

while x < 10:
  if x == 5:
    break
  print(x)
  x +=1

x = 0

while x < 10:
  if x == 5:
    break
  print(x)
  x +=1
