"""
COMANDOS BÁSICOS EM PYTHON 11 - Módulo CSV (Leitura, estrica e parsing)
    Autor: Júlia Onora da Silva
    Data: 6 de janeiro de 2022
"""

import csv

with open("teste.csv", "r") as csv_file:
  csv_reader = csv.reader(csv_file)

  with open("novo_csv.csv", "w") as new_file:
    csv_writer = csv.writer(new_file, delimiter="\t")

    for line in csv_reader:
       csv_writer.writerow(line)