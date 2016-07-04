---
layout: post
title: 10 Docstrings 02
date:  2016-07-04 01:00:00
---
Docstring
: Cadena de documentació d’atribut.

Referència a altres arxius que parlen de [docstrings](/python/2016/07/02/docstrings.html)
    
Partim del següent codi que el podem guardar en un arxiu anomenat `triangle.py`:

    def area_triangle(base, altura):
        '''(number,number) -> number
        Retorna l'àrea d'un rectangle al passar-li la base i l'altura
        '''
        area = (base + altura)/2
        return area

    def perimetre_triangle(a,b,c):
        perimetre = (a+b+c)
        return perimetre

Així doncs, hem documentat el `docstring` amb aquesta informació:

	'''(number,number) -> number
		Retorna l'àrea d'un rectangle al passar-li la base i l'altura
	'''

D'aquesta manera, quan estrem escrivint area_triangle en `IDL3` ens eixirà l'ajuda en un finestreta.

Font: Videotutoriales [12](https://www.youtube.com/watch?v=EGfG7Hs93G0&index=13&list=PLEtcGQaT56chpYflEjBWRodHJNJN8EKpO)


