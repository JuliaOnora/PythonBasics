"""
COMANDOS BÁSICOS EM PYTHON 1 - Funcionalidades de texto
    Autor: Júlia Onora da Silva
    Data: 6 de janeiro de 2022
"""

mensagem = "Hello Word!"
print(mensagem)

mensagem = "Júlia\'s Code :)"
print(mensagem)

"""Cada célula possui escopo local."""

mensagem = """Aqui
serão
apresentadas
algumas
anotações"""
print(mensagem)

mensagem = "ABCDE"
print("Tamanho: ", len(mensagem))

print("Segundo caracter: ", mensagem[1])

print("Quatro primeiros cacteres: ", mensagem[0:4])

print("Quatro primeiros cacteres ainda: ", mensagem[:4])

print("Fazendo o slicing dos dois últimos carcteres: ", mensagem[3:])

print("Todos caracteres em letras minúsculas: ", mensagem.lower())

print("E agora maiúsculas: ", mensagem.upper())

print(f"Contando quantas vezes \'C\' aparece emm {mensagem}: ", mensagem.count("C"))

print("Enquanto o comando \'find\' encontra em qual index \'C\' aparece: ", mensagem.find("C"))

"""Aqui, os index se iniciam na posição zero."""

print("Quantas vezes \'Z\' aparece: ", mensagem.find("Z"))

"""Index igual a "-1" indica que o caracter especificado não aparece na string."""

mensagem_nova = mensagem.replace("C","Z")
print("Substituir um caracter (C por Z): ", mensagem_nova)

print("Combinando strings\n")
comeco = "Olá"
nome = "Fulano"

frase = comeco + ', ' + nome + '!'
print(frase)

print("Ou ainda: \n")
print(f"{comeco}, {nome.upper()}!")

print("Lista de atributos que podem ser atribuídos à string indicada: ", dir(nome))

print("Imprimindo o código de auxílio: ", help(nome.upper))

# Também poder ser visto por
help(nome.upper)
