#!/usr/bin/python3.4
# -*- coding: utf-8 -*-
# arxiu = 'mcm.py'
# objectiu = 'Calcular el MCM de dos numeros'
# versio = '0.1'
# llicencia = '$MIT'
# autor = 'Alfons Rovira'
# data = '2016/07/24'

# Definim funcio

def mcm(x,y):
    '''Aquesta funcio reb dos sensers i torna un multiple comu'''

    # Agafem el major dels dos
    if x > y:
        major = x
    else:
        major = y

    while(True):
        if((major % x == 0) and (major % y == 0)):
            mcm = major
            break
        major += 1

    return mcm

# Sol·licitem els dos nombres
nom1 = int(input('Introdueix el primer nombre:'))
nom2 = int(input('Introdueix el primer nombre:'))

print('El minim comu multiple de ', nom1,'i', nom2,' es ', mcm(nom1, nom2))

