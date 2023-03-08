"""
COMANDOS BÁSICOS EM PYTHON 9 - Funções para trabalhar com Sistema Operacional
    Autor: Júlia Onora da Silva
    Data: 6 de janeiro de 2022
"""

import os

print("Atributos e métodos: ", dir(os))

print("Diretório atual: ", os.getcwd())

print("Lista de diretórios: ", os.listdir())

# Criar novo diretório

os.mkdir("novo_dir")
print("Lista de diretórios: ", os.listdir())

# Deletar um diretório

os.rmdir("novo_dir")
print("Lista de diretórios: ", os.listdir())

# Renomear

os.mkdir("novo_dir")
print("Lista de diretórios: ", os.listdir())
os.rename("novo_dir", "novo_novo_dir")
print("Lista de diretórios: ", os.listdir())

print("Status do diretório criado\n", os.stat("novo_novo_dir"))

from datetime import datetime

data_mod = os.stat("novo_novo_dir").st_mtime
print("Data de modificação do diretório: ", datetime.fromtimestamp(data_mod))

os.rmdir("novo_novo_dir")
print("Lista de diretórios: ", os.listdir())

# Sabendo o local

print(os.environ.get('HOME'))
