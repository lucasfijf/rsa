import random

class GeneratePrimeNumber:

    def __init__(self) -> None:
        self.bits = 8
    
    def generate(self) -> int:
        number = self.__get_random_number()
        while not self.__primality_test(number):
            number = self.__get_random_number()
        return number

    def __get_random_number(self) -> int:
        bits_length = self.bits
        number = random.getrandbits(bits_length)
        return number
    
    def __primality_test(self, number: int) -> bool:
        if number <= 3:
            return number > 1
        if number % 2 == 0 or number % 3 == 0:
            return False
        limit = int(number ** 0.5)
        for n in range(5, limit):
            if number % n == 0 or number % (n + 2) == 0:
                return False
        return True