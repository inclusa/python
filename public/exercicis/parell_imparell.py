# Programa: parell_imparell.py
# Objectiu: Calcular si el nombre donat es parell
# Autor: John Smith
# Data: 2016-07-07

# Obtenim les dades

x = int(input('Nombre: '))
y = int(2)

# Calculant

if x % y == 0:
    print('Es nombre parell')

if x % y != 0:
    print('Es nombre imparell')