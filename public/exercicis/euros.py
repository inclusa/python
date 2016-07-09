#!/usr/bin/python3.4
# -*- coding: utf-8 -*-
#__program = 'euros.py'
#__goal__ = 'Calcular el desglosament minim en bitllets i en monedes €'
#__version__ = '0.1'
#__license__ = 'MIT'
#__author__ = 'Alfons Rovira'
#__date__ = '2016/07/08'

from math import floor

# Introduccio de dades
x = int(input('Nombre: '))

# Variables
a = x / int(200) # Quocient
aa = x % int(200) # Residu

b = x % int(100) # Residu

c = x % int(50) # Residu

d = x % int(20) # Residu

e = x % int(10) # Residu

f = x % int(5) # Residu

g = x % int(2) # Residu



if aa == 0: # Dividim entre bitllets de 200 €
    print('Bitllets de 200 €', a)

else:
    print('Bitllets de 200 €: ', int(a), '€')
    print('Bitllets de 100 €: ', int(aa/int(100)), '€')
    print('Bitllets de 50 €:  ', int(b/int(50)), '€')
    print('Bitllets de 20 €:  ', int(c/int(20)), '€')
    print('Bitllets de 10 €:  ', int(d/int(10)), '€')
    print('Bitllets de 5 €:   ', int(e/int(5)), '€')
    print('Bitllets de 2 €:   ', int(f/int(2)), '€')
    print('Bitllets de 1 €:   ', int(g/int(1)), '€')
