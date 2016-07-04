---
layout: post
title: 13 Convertir
date:  2016-07-04 04:00:00
---

	>>> a = 2
	>>> b = '3'
	>>> a + b
	Traceback (most recent call last):
	  File "<pyshell#2>", line 1, in <module>
	    a + b
	TypeError: unsupported operand type(s) for +: 'int' and 'str'

Per tal de convertir dades utilitzarem aquestes funcions:

- `int()`
- `float()`
- `str()`

Convertirem les dades per tal que es puguen **sumar** les variables (integer) i després tornarem a convertir aquestes variables per **contatenar-les** (string).

	>>> a = 2
	>>> b = '3'
	>>> a + b
	Traceback (most recent call last):
	  File "<pyshell#2>", line 1, in <module>
	>>> int(b)
	3
	>>> a + b
	Traceback (most recent call last):
	  File "<pyshell#5>", line 1, in <module>
	    a + b
	TypeError: unsupported operand type(s) for +: 'int' and 'str'
	>>> a + int(b)
	5

Ara convertirem la variable `a` a `string` i concatenarem les variables.

	>>> str(a) + b
	'23'

També podem convertir a `float` aquestes dues variables.

	>>> float(a)
	2.0
	>>> float(b)
	3.0

Exemple:

	>>> def falten_proves():
		proves_totals = 12
		proves_passades = input('Quantes proves has passat?')
		diferencia =proves_totals - int(proves_passades)
		diferencia =str(diferencia)
		return 'Te falten per passar un total de ' + diferencia + 'proves '
	
	>>> falten_proves()
	Quantes proves has passat?7
	'Te falten per passar un total de 5 proves'

Font: Videotutoriales [15](https://www.youtube.com/watch?v=ac1_pL19TQM&index=16&list=PLEtcGQaT56chpYflEjBWRodHJNJN8EKpO)
 
