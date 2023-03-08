"""
COMANDOS BÁSICOS EM PYTHON 12 - Módulo Datetime (Dates, Times, Timedeltas, and Timezones)
    Autor: Júlia Onora da Silva
    Data: 6 de janeiro de 2022
"""

import datetime

data1 = datetime.date(2022, 1, 6) # ano, mês e dia, respetivamente
print(data1)

data2 = datetime.date.today()
print(data2) 
print("Dia: ", data2.day)
print("Mês: ", data2.month)
print("Ano: ", data2.year)

print("Dia da semana: (semana começa na segunda-feira, index 0): ", data2.weekday())
print("Dia da semana: (semana começa no domingo): ", data2.isoweekday())

tdelta = datetime.timedelta(days=7)
print("Daqui a uma semana: ", tdelta + data2)

birth = datetime.date(1999, 7, 18)
dias_ate_a = data2 - birth
print("Tempo até o aniversário: ", dias_ate_a.days, " dias")

t = datetime.time(3, 30, 45, 10234)
print("Hora formatada: ", t)

t2 = datetime.datetime(data2.year, data2.month, data2.day, 3, 30, 45, 10234)
print(t2)
print(t2.date())
print(t2.time())
