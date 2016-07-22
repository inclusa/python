class Humano:
    def __init__(self):
        self.edad = 15
        print('Soy un objeto')

    def hablar(self,mensaje):
        print('mensaje')

pedro = Humano()
raul = Humano()

print('Soy Pedro y tengo', pedro.edad)
print('Soy Raul y tengo', pedro.edad)

pedro.hablar('hola')
raul.hablar('Hola, Pedro')
