#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__program = 'equacio.py'
#__goal__ = 'Resolucio equacio de 2n grau'
#__version__ = '0.1'
#__license__ = 'MIT'
#__author__ = 'Alfons Rovira'
#__date__ = '2016/07/09'


#importem l'arrel quadrada del modul math

from math import sqrt

print('Resolucio de l\'equacio ax**2 + bx + c = 0')

a = float(input('Valor de a:'))
b = float(input('Valor de b:'))
c = float(input('Valor de c:'))

if a != 0:
    x1 = (-b + sqrt(b**2 - 4*a*b)) / 2*a
    x2 = (-b - sqrt(b**2 - 4*a*b)) / 2*a
    print=('Solucions x1 = {0:.3f} i x2 = {1:.3f}'.format(x1,x2))

else:
    print('No es una equacio de segon grau')