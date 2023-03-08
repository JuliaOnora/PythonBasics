"""
COMANDOS BÁSICOS EM PYTHON 2 - Funcionalidades de números inteiros e de ponto flutuante
    Autor: Júlia Onora da Silva
    Data: 6 de janeiro de 2022
"""

num1 = 3
num2 = 4.0

print("Nro inteiro: ", num1, type(num1))
print("Nro com ponto flutuante/float: ", num2, type(num2))

# Operaç~eos matemáticas

print(f"Adição entre {num1} e {num2}: ", num1+num2)
print(f"Subtração entre {num1} e {num2}: ", num1-num2)
print(f"Multiplição entre {num1} e {num2}: ", num1*num2)
print(f"Divisão entre {num1} e {num2}, considerando casas decimais: ", num1/num2) 
print(f"Divisão entre {num1} e {num2}, descartando as casa decimais: ", num1//num2)
# Resultado de um divisão sempre será um nro float

print(f"Exponenciação de {num1} elevado a {num2}: ", num1**num2)
print(f"Encontrando o resto da divisão de {num1} por {num2}: ", num1%num2)

print("Resto da divisão de um nro par por 2:", num2%2)
print("Resto da divisão de um nro ímpar por 2:", num1%2)

num3 = -3.75

print("Valor absoluto do número 3: ", abs(num3))
print("Valor arredondado do número 3, para 1 casa decimal: ", round(num3,1))

# Operadores de comaparação, retornam valores booleanos

print("Nro 1: ", num1)
print("Nro 2: ", num2)

print("Número 1 é igual ao número 2! ", num1==num2)
print("Número 1 é diferente do número 2! ", num1!=num2)
print("Número 1 é maior que o número 2! ", num1>num2)
print("Número 1 é menor que o número 2! ", num1<num2)
print("Número 1 é maior ou igual ao número 2! ", num1>=num2)
print("Número 1 é menor ou igual ao número 2! ", num1<=num2)

num4 = '5'
num5 = '6'

print(num4+num5)

"""Concatena "num4" e "num5" por aqui essa variáveis são strings. A correção do problema ocorre fazendo o casting das variáveis"""

# Casting: forçar a formatação do tipo de uma variável
num4 = int('5')
num5 = int('6')

print(num4+num5)
