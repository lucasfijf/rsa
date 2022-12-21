import math
import random

def generate_prime_number():

    initial_range = 2**10
    final_range = 3**10

    while True:
        number = random.randint(initial_range, final_range)
        for i in range(2, int(number/2) + 1):
            if number % i == 0:
                break
        else:
            return number

def generate_coprime_number(phi):

    final_range = phi + 1
    while True:
        coprime = random.randint(1, final_range)
        if math.gcd(coprime, phi) == 1:
            return coprime

def modular_multiplicative_inverse(e, phi):

    for number in phi - 1:
        if (e * number) % phi == 1:
            return number

# p = generate_prime_number()
# q = generate_prime_number()

p = 3
q = 11

test = (p - 1) * (q - 1)
print(test)
print(generate_coprime_number(test))

def generate_key():

    n = p * q
    # Euler's totient function
    phi = (p - 1) * (q - 1)
    e = generate_coprime_number(phi)
    d = modular_multiplicative_inverse(e, phi)
    
