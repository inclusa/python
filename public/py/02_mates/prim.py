#Lista de numeros primos entre 1 y 100 en una sola linea
c = [i for i in range(2,101) if (i%2!=0 or i==2) and (i%3!=0 or i==3) and (i%5!=0 or i==5) and (i%7!=0 or i==7)]
print (c)
