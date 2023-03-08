"""
COMANDOS BÁSICOS EM PYTHON 3 - Listas, tuplas e sets
    Autor: Júlia Onora da Silva
    Data: 6 de janeiro de 2022
"""

cursos = ['Engenharia', 'Medicina', 'História', 'Psicologia']

print("Graduações: ", cursos)
print("Quantas graduações existem? ", len(cursos))
print("Primeira graduação da lista: ", cursos[0])
print("Última graduação da lista: ", cursos[-1])
print("Penúltima graduação da lista: ", cursos[-2])

# Slicing de uma lista

print("Dois primeiros cursos de graduação da lista: ", cursos[0:2])
print("Ainda os dois primeiros cursos de graduação da lista: ", cursos[:2])
print("Dois últimos cursos de graduação da lista: ", cursos[2:])

# Adicionar um ítem ao ninal da lista

cursos.append('Arte')
print("Graduações: ", cursos)

# cursos.insert(0, 'Arte')
# print("Graduações, colocando Arte no começo da lista: ", cursos)

cursos2 = ['Física', 'Ciência Contábeis']
cursos.extend(cursos2)
print("Graduações: ", cursos)

# Removendo itens da lista

cursos.remove('Arte')
print("Graduações: ", cursos)

# Escrevendo a lista ao contrário

cursos.reverse()
print("Lista em ordem alfabética: ", cursos)

# Ordenando em ordem alfabética uma lista

cursos.sort()
print("Lista em ordem alfabética: ", cursos)

# Ordenando de forma crescente uma lista

nros = [2, 3, 5, 7, 1]
nros.sort()
print("Lista em ordem crescente: ", nros)

# Valor mínimo, máximo e soma de um lista de nros

print("Lista: ", nros)
print("Valor mínimo: ", min(nros))
print("Valor máximo: ", max(nros))
print("Somatório: ", sum(nros))

# Encontrando o index de um valor em uma lista

print("Lista: ", nros)
print("Index do valor 2: ", nros.index(2))

print("Lista de cursos: ", cursos)
print("Arte está na lista! ", 'Arte' in cursos)

for i in cursos:
  print(i)

for index, i in enumerate(cursos):
  print("Index: ", index, "Nome: ", i)

# Formar uma string de uma lista de strings

cursos_frase = ', '.join(cursos)
print("Cursos: ", cursos_frase)

# Transportando em lista novamente

nova_frase = cursos_frase.split(', ')
print("Cursos: ", nova_frase)

# Tuplas, não são modificáveis

tupla = ('Arte', 'História')
tupla[0] = 'Geografia'

# Sets, ordenações aleatórias

set1 = {'Arte', 'História', 'Geografia'}
set2 = {'Psicologia', 'História', 'Engenharia'}

print("Interseções: ", set1.intersection(set2))
print("Diferenças: ", set1.difference(set2))
print("Junção: ", set1.union(set2))

# Criando listas, tuplas e sets vazios

vazio1 = []
vazio2 = list()
vazio3 = ()
vazio4 = tuple()
vazio5 = set()

print("Quantos itens tem as listas, tuplas e sets criadas? ", len(vazio1), len(vazio2), len(vazio3), len(vazio4), len(vazio5))