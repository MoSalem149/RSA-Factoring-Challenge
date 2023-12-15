#!/usr/bin/python3
import time
import math
import sys

def pollard_rho_algorithm(n):
    if n % 2 == 0:
        return 2

    A = 2
    B = 2
    C = 1

    F = lambda A: (A**2 + 1) % n

    while C == 1:
        A = F(A)
        B = F(F(B))
        C = math.gcd(abs(A - B), n)

    return C

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def factorize_and_print(number):
    P = pollard_rho_algorithm(number)

    while not is_prime(P):
        P = pollard_rho_algorithm(P)

    Q = number // P

    if P == number or Q == number:
        print(f"{number} is prime.")
    else:
        print(f"{number}={P}*{Q}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python factorize.py <file>")
        return

    file_path = sys.argv[1]

    start_time = time.time()
    try:
        with open(file_path, 'r') as file:
            number = int(file.readline().strip())

        factorize_and_print(number)

        if time.time() - start_time > 5:
            print("Time limit exceeded")
            exit()

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except ValueError:
        print("Error: Invalid input in the file. Please ensure the file contains a valid natural number.")


if __name__ == '__main__':
    main()
