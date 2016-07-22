# arxiu = 'humano.py'
# objectiu = 'Estudiar les classes'
# versio = '0.1'
# llicencia = '$MIT'
# autor = 'Alfons Rovira'
# data = '2016/07/22'

class Humano:
    def __init__(self):
        print('Soy un objeto')

    def hablar(self,mensaje):
        print('mensaje')

pedro = Humano()
raul = Humano()

pedro.hablar('hola')
raul.hablar('Hola, Pedro')