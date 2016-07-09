from math import pi

cadena_leida = input()
radio = float(cadena_leida)
volumen = 4/3 * pi * radio** 3

print(volumen)
print("Volumen:", volumen)
print("Volumen: {0:.2f} metres cubics" .format(volumen), end='')