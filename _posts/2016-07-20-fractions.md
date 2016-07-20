---
layout: post
title: 34 Fractions
date:  2016-07-20 00:00:00
---

Interessant funció dins del mòdul `fractions` ens dóna informació molt interessant per tal de recolzar l'estudi de les fraccions.

Així doncs, porem saber la fracció irreduïble de forma molt fàcil.

```python
>>> from fractions import Fraction
>>> Fraction(30,15)
Fraction(2, 1)
>>> Fraction()
Fraction(0, 1)
>>> Fraction(321,33)
Fraction(107, 11)
>>> Fraction(56/21)
Fraction(6004799503160661, 2251799813685248)
>>> Fraction('56/21')
Fraction(8, 3)
```

Font: [Documentació de Python. 9.5 Fractions - Rational numbers](https://docs.python.org/3.1/library/fractions.html)
