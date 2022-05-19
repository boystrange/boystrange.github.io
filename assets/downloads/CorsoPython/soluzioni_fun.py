#!/usr/bin/env python3

from functools import reduce
import operator

#########################
# soluzione esercizio 1 #
#########################

def factorial(n):
    assert n >= 0
    return reduce(operator.mul, range(1, n + 1), 1)

assert factorial(10) == 3628800

#########################
# soluzione esercizio 2 #
#########################

def coefficient(a, k):
    l = [ a - h for h in range(k) ]
    return reduce(operator.mul, l, 1) / factorial(k)

assert coefficient(4, 2) == 6

#########################
# soluzione esercizio 3 #
#########################

def integrate(f, a, b, n):
    assert n > 0
    h = (b - a) / n
    samples = [ f(a + i * h) for i in range(n) ]
    areas = [ b * h for b in samples ]
    return reduce(operator.add, areas, 0)

#########################
# soluzione esercizio 4 #
#########################

def add_vectors(V, W):
    assert len(V) == len(W)
    return [ x + y for x, y in zip(V, W) ]

def mul_vectors(V, W):
    assert len(V) == len(W)
    U = [ x * y for x, y in zip(V, W) ]
    return reduce(operator.add, U, 0)

#########################
# soluzione esercizio 5 #
#########################

def rows(M): return len(M)

def cols(M): return len(M[0])

def transpose(M):
    return [ [ row[j] for row in M ] for j in range(cols(M)) ]

M = [[1, 4, 6, 10],
     [2, 7, 5, 3]]

assert transpose(transpose(M)) == M

#########################
# soluzione esercizio 6 #
#########################

def mul_matrices(M, N):
    assert cols(M) == rows(N)
    return [ [ mul_vectors(row, col) for col in transpose(N) ] for row in M ]

N = [[1, 4, 6],
     [2, 7, 5],
     [9, 0, 11],
     [3, 1, 0]]
R = [[93, 42, 92],
     [70, 60, 102]]

assert mul_matrices(M, N) == R

#########################
# soluzione esercizio 7 #
#########################

def trapezoids(f, a, b, n):
    h = (b - a) / n
    samples = [ f(a + i * h) for i in range(n + 1) ]
    areas = [ (b + B) * h / 2 for (b, B) in zip(samples, samples[1:]) ]
    return reduce(operator.add, areas, 0)

#########################
# soluzione esercizio 8 #
#########################

def is_sorted(xs):
     ys = zip(xs, xs[1:])
     zs = [ x <= y for x, y in ys ]
     return reduce(operator.and_, zs, True)

assert is_sorted(range(1, 100, 3))