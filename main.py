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

    # coprime_number = []
    # for number in range(2, phi):
    #     if math.gcd(phi, number) == 1 and modular_multiplicative_inverse(number, phi) != None:
    #         coprime_number.append(number)
    # for element in coprime_number:
    #     if element == modular_multiplicative_inverse(element, phi):
    #         coprime_number.remove(element)
    # return coprime_number

    # number = phi + 1
    # coprime = random.randint(1, number)
    # return coprime
    final_range = phi + 1
    while True:
        coprime = random.randint(1, final_range)
        if math.gcd(coprime, phi) == 1:
            return coprime



def modular_multiplicative_inverse():

    pass



p = generate_prime_number()
q = generate_prime_number()

test = (p - 1) * (q - 1)
print(test)
print(generate_coprime_number(test))

def generate_key():

    n = p * q
    # Euler's totient function / phi
    phi = (p - 1) * (q - 1)
    e = generate_coprime_number(phi)
    d = modular_multiplicative_inverse(e)
    
