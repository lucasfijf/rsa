import random
from typing import Type
from .generate_prime_number import GeneratePrimeNumber

class GenerateKeys:

    def __init__(self, prime_number_generator: Type[GeneratePrimeNumber]) -> None:
        self.p = prime_number_generator.generate()
        self.q = prime_number_generator.generate()
    
    def generate(self) -> dict:
        p = self.p
        q = self.q
        n = p * q
        phi = (p - 1) * (q - 1)
        e = self.__coprime(phi)
        d = self.__modular_multiplicative_inverse(e, phi)
        keys = {
            "n": n,
            "e": e,
            "d": d
        }
        return keys

    def __coprime(self, phi: int) -> int:
        number = random.randint(2, phi)
        while not self.__gcd(number, phi) == 1:
            number = random.randint(2, phi)
        return number

    def __gcd(self, a: int, b: int) -> dict:
        while b != 0:
            a, b = b, a % b
        return a

    def __modular_multiplicative_inverse(self, a: int, m: int) -> int:
        for number in range(1, m):
            if (a * number) % m == 1:
                return number
        return None