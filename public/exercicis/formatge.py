# Programa: formatge.py
# Objectiu: Calcular el tant per cent de les notes
# Autor: John Smith
# Data: 2016-07-07

from turtle import Screen, Turtle

# Qualificacions

suspensos = 10
aprovats = 20
notables = 40
excel = 30

# Radi del cercle

radi = 300

# Inicialitzacio

pantalla = Screen()
tortuga = Turtle()
tortuga.speed(0)

# Dibuix del cercle exterior

tortuga.penup()
tortuga.goto(0, -radi)
tortuga.pendown()
tortuga.circle(radi)
tortuga.penup()
tortuga.home()
tortuga.pendown()

# Dibuix de la linia per als suspensos

angul = 360 * suspensos / 100
tortuga.left(angul)
tortuga.forward(radi)
tortuga.backward(radi)

# Escriture el text per als suspensos

tortuga.penup()
tortuga.right(angul / 2)
tortuga.forward(radi / 2)
tortuga.write('suspensos')
tortuga.backward(radi / 2)
tortuga.left(angul / 2)
tortuga. pendown()

# Dibuix de la linia per als aprovats

angul = 360 * aprovats / 100
tortuga.left(angul)
tortuga.forward(radi)
tortuga.backward(radi)

# Escriture el text per als aprovats

tortuga.penup()
tortuga.right(angul / 2)
tortuga.forward(radi / 2)
tortuga.write('aprovats')
tortuga.backward(radi / 2)
tortuga.left(angul / 2)
tortuga. pendown()

# Dibuix de la linia per als notables

angul = 360 * notables / 100
tortuga.left(angul)
tortuga.forward(radi)
tortuga.backward(radi)

# Escriture el text per als notables

tortuga.penup()
tortuga.right(angul / 2)
tortuga.forward(radi / 2)
tortuga.write('notables')
tortuga.backward(radi / 2)
tortuga.left(angul / 2)
tortuga. pendown()

# Dibuix de la linia per als exel·lents

angul = 360 * excel / 100
tortuga.left(angul)
tortuga.forward(radi)
tortuga.backward(radi)

# Escriture el text per als excel·lents

tortuga.penup()
tortuga.right(angul / 2)
tortuga.forward(radi / 2)
tortuga.write('excel')
tortuga.backward(radi / 2)
tortuga.left(angul / 2)
tortuga. pendown()

# Eixir quan es polse el boto a la finestra
pantalla.exitonclick()