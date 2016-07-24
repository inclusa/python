#!/usr/bin/env python
# -*- coding: utf-8 -*-

# arxiu = 'mdc.py'
# objectiu = 'Hallar el Maxim Comu Divisior de dos nombres'
# versio = '0.1'
# llicencia = '$MIT'
# autor = 'Alfons Rovira'
# data = '2016/07/24'

# Definim la funcio

def mcd(a, b):
    residu = 0
    while(b > 0):
        residu = b
        b = a % b
        a = residu
    return a

# Sol·licitem els dos nombres

nom1 = int(input('Introdueix el primer: '))
nom2 = int(input('Introdueix el segon: '))

print('El maxim comu divisor de ', nom1,' i ', nom2,' es ', mcd(nom1, nom2))