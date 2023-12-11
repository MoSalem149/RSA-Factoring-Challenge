#!/usr/bin/python3
import sys
from math import sqrt

def factorize(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return i, n // i
    return n, 1

def main(filename):
    with open(filename, 'r') as file:
        lines = file.read().splitlines()

    for line in lines:
        number = int(line)
        factor1, factor2 = factorize(number)
        print("{}={}*{}".format(number, factor2, factor1))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        sys.exit(1)

    filename = sys.argv[1]
    main(filename)
