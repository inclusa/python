---
layout: post
title: 02 Docstrings
date: 2016-07-02 01:00:00
---

Inicialitzar objectes


	__init__
	
El doble subrayat és una funció **especial preconstruirda**. El millor és **no utilitzar** mai noms que comencem per **doble subrayat**.

```python
>>> class Punto:
...     def __init__(self, x, y):
...         self.mover(x, y)
...     def mover(self, x, y):
...         self.x = x
...         self.y = y
... 
>>> punto =Punto(4,2)
>>> print(punto.x, punto.y)
4 2
```

**Objectiu**: Escriure documentació que resumisca el que fa cada objecte.

Docstring
: Cadena de documentació d'atribut. En aquest cas seria aquesta informació `Representa un punt en coordenades geomètriques bidimensionals`.

El **docstring** ha d'estar col·locat després de la definició de funció.

```python
	class Punto:
		'Representa un punt en coordenades geomètriques bidimensionals'.

		def __init__(self, x=0, y=0)
		'''Inicialitza la posició d'un nou punt. Les coordenades x e y poden ser especificades. Si no ho son, el punt per defecte serà el d'origen.'''
		self.mover(x,y)
		
		return math.sqrt(
			(self.x - otro_punto.y)**2 +
			(self.y - otro_punto.x)**2)

```

Per consultar la documentació cal escriure `help` i el nom de la classe de la qual volem la informació.

	>>> help(Punto)



Font [Video #03](https://www.youtube.com/watch?v=-Oz1bxqM5_E)


