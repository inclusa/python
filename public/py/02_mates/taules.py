#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Arxiu = 'taules.py'
# Objectiu = 'Imprimir taules de multiplicar'
# Versio = '0.1'
# Llicencia = '$MIT'
# Autor = 'Alfons Rovira'
# Data = '2016-07-25'


t = '-'

for x in range(1, 11):
    print(t*50)
    print(repr(x).rjust(3), end='')
    print(repr(2 * x).rjust(5), end='')
    print(repr(3 * x).rjust(5), end='')
    print(repr(4 * x).rjust(5), end='')
    print(repr(5 * x).rjust(5), end='')
    print(repr(6 * x).rjust(5), end='')
    print(repr(7 * x).rjust(5), end='')
    print(repr(8 * x).rjust(5), end='')
    print(repr(9 * x).rjust(5), end='')
    print(repr(10 * x).rjust(5), end='\n')

