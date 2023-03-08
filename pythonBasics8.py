"""
COMANDOS BÁSICOS EM PYTHON 8 - Importação de módulos e bibliotecas padrões
    Autor: Júlia Onora da Silva
    Data: 6 de janeiro de 2022
"""

import random

nros = [1, 2, 3, 4, 5]

aleat = random.choice(nros)
print("Valor aleatório da lista: ", aleat)

import math

angulo = 90 # graus

radiano = math.radians(angulo)

print(f"{angulo} em radianos são: ", radiano)

from datetime import date
import calendar

hoje = date.today()

print("Hoje são dia ", hoje)

if calendar.isleap(hoje.year):
  print("Estamos num ano bisexto ")

else:
  print("Não estamos num ano bisexto")

import os

print("Diretório atual: ", os.getcwd())
print("Diretório atual: ", os.__file__)