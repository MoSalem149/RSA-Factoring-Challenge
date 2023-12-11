#!/usr/bin/python3
import sys
from math import sqrt

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def pollards_rho(n):
    x, y, d = 2, 2, 1
    f = lambda x: (x**2 + 1) % n

    while d == 1:
        x = f(x)
        y = f(f(y))
        d = gcd(abs(x - y), n)

    return d

def factorize_rsa(n):
    factors = []

    while n % 2 == 0:
        factors.append(2)
        n //= 2

    while n > 1 and n != 0:
        if n > 2**64:
            factor = pollards_rho(n)
        else:
            factor = factorize_small(n)
        factors.append(factor)
        n //= factor

    return factors[::-1]  # Reverse the order of factors

def factorize_small(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return i
    return n

def main(filename):
    with open(filename, 'r') as file:
        lines = file.read().splitlines()

    for line in lines:
        number = int(line)
        factors = factorize_rsa(number)
        primes = [factor for factor in factors if is_prime(factor)]
        print("{}={}".format(number, '*'.join(map(str, primes))))

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: rsa <file>")
        sys.exit(1)

    filename = sys.argv[1]
    main(filename)
