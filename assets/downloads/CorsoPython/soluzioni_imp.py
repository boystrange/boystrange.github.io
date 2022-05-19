#########################
# soluzione esercizio 1 #
#########################

def sum_all(n):
    assert n >= 0
    s = 0
    while n > 0:
        s += n
        n -= 1
    return s

print(sum_all(10))

#########################
# soluzione esercizio 2 #
#########################

def prime(n):
    assert n >= 0
    d = 2
    while d <= n // 2:
        if n % d == 0: return False
        d += 1
    return n > 1

def print_primes(n):
    i = 0
    while i <= n:
        if prime(i): print(i)
        i += 1

print_primes(20)

#########################
# soluzione esercizio 3 #
#########################

def first_prime(n):
    while not prime(n):
        n += 1
    return n

#########################
# soluzione esercizio 4 #
#########################

def ones(n):
    assert n >= 0
    c = 0
    while n > 0:
        if n % 2 == 1: c += 1
        n //= 2
    return c

print(ones(15), ones(16))
