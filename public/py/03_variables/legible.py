# Programa: llegible.py
# Objectiu: Calcular el perimetre i l'area del rectangle a partir de l'altura i l'amplada
# Autor: John Cleese
# Data: 01/01/2010

# Peticio de dades en metres
print("Programa per al calcul de l\'altura i de l\'area del rectangle")

altura = float(input("Donam l\'altura: "))
amplada = float(input("Donam l\'amplada: "))

# Calcul de l'area i del perimetre'
area = altura * amplada
pemimetre = 2 * altura + 2 * amplada

# Impressio dels resultats per pantalla
print("El perimetre es de: {0:6.2f} metres" .format(pemimetre))
print("L\'area es de: {0:6.2f} metres quadrats" .format(area))