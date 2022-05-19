#!/usr/bin/env python3

#########################
# soluzione esercizio 1 #
#########################

def factorial(n):
    assert n >= 0
    r = 1
    for i in range(2, n + 1):
        r *= i
    return r

assert factorial(10) == 3628800

#########################
# soluzione esercizio 2 #
#########################

def divisors(n):
    assert n >= 0
    return [ i for i in range(1, n + 1) if n % i == 0 ]

assert divisors(99) == [1, 3, 9, 11, 33, 99]

#########################
# soluzione esercizio 3 #
#########################

def prime(n):
    assert n >= 0
    return [1, n] == divisors(n)

assert prime(101)

#########################
# soluzione esercizio 4 #
#########################

def pivot(l, x):
    return ([ m for m in l if m <= x],
            [ m for m in l if m > x])

assert pivot(divisors(99), 20) == ([1, 3, 9, 11], [33, 99])

#########################
# soluzione esercizio 5 #
#########################

def is_sorted(l):
    if l == []: return True
    prev = l[0]
    for x in l[1:]:
        if prev > x: return False
        prev = x
    return True

assert is_sorted(divisors(99))
