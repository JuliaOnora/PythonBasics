"""
COMANDOS BÁSICOS EM PYTHON 13 - Ordenação de listas, tuplas e objetos
    Autor: Júlia Onora da Silva
    Data: 6 de janeiro de 2022
"""

lista = [5, 4, 1, 8]

lista_o = sorted(lista)
print("Copia a lista indicada ordenada: ", lista_o)

lista.sort()
print("Lista original ordenada: ", lista)

lista_o = sorted(lista, reverse=True)
print("Copia a lista indicada ordenada no reverso: ", lista_o)

lista.sort(reverse=True)
print("Lista original ordenada: ", lista)

tupla = (5, 4, 1, 8)

# como não é possível modificar tuplas, só funciona a fução sorted()

tupla_o = sorted(tupla)
tupla_o2 = sorted(tupla, reverse=True)
print("Tupla ordenada: ", tupla_o)
print("Tupla ordenada no reverso: ", tupla_o2)