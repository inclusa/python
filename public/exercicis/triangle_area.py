from math import sqrt

costat_1 = 2
costat_2 = 3
costat_3 = 4

a = int(costat_1)
b = int(costat_2)
c = int(costat_3)

s = (a + b + c) / 2

area = sqrt(s * (s - a) * (s - b) * (s - c))

print("Area: "area)

