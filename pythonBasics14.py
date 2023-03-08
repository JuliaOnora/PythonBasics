"""
COMANDOS BÁSICOS EM PYTHON 14 - Tratamento de erros (Bloco try/except)
    Autor: Júlia Onora da Silva
    Data: 6 de janeiro de 2022
"""

try:
  f = open('teste.txt')
except:
  print("I can't")


try:
  f = open('teste_.txt')
except Exception as e:
    print(e)
except:
  print("I can't")


try:
  f = open('teste.txt')
except Exception as e:
    print(e)
except:
  print("I can't")
else:
  print(f.read())
  f.close()

try:
  f = open('teste.txt')
except Exception as e:
    print(e)
except:
  print("I can't")
else:
  print(f.read())
  f.close()
finally:
  print("Executando...")
