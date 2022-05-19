
import math

#########################
# soluzione esercizio 1 #
#########################

def sum_all(n):
    assert n >= 0
    return n * (n + 1) // 2

print(sum_all(10))

#########################
# soluzione esercizio 2 #
#########################

def lato(n, r):
    assert n > 2 and r >= 0
    return 2 * r * math.sin(math.pi / n)

def apotema(n, r):
    assert n > 2 and r >= 0
    return r * math.cos(math.pi / n)

def perimetro(n, r):
    return n * lato(n, r)

def area(n, r):
    return n * lato(n, r) * apotema(n, r) / 2

print("lato quadrato raggio 1 = ", lato(4, 1))
