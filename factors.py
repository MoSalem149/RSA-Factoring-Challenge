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

def main():
    if len(sys.argv) != 2:
        print("Usage: ./factors <file>")
        return

    file_path = sys.argv[1]
    start_time = time.time()

    try:
        with open(file_path, 'r') as file:
            nums = file.readlines()

        for num in nums:
            current_num = int(num.strip())
            factor = pollard_rho_algorithm(current_num)

            if factor == current_num:
                print(f"{current_num} is prime.")
            else:
                print(f"{current_num}={factor}*{current_num // factor}")

            if time.time() - start_time > 5:
                print("Time limit exceeded")
                exit()

    except FileNotFoundError:
        print(f"File '{file_path}' not found.")

if __name__ == '__main__':
    main()
