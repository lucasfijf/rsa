from src.generate_prime_number import GeneratePrimeNumber
from src.generate_keys import GenerateKeys
from src.rsa_algorithm import RSA


def menu():
    should_continue = True
    print("\nGenerating your keys...")
    prime_number = GeneratePrimeNumber()
    generate_keys = GenerateKeys(prime_number)
    keys = generate_keys.generate()
    n = keys["n"]
    e = keys["e"]
    d = keys["d"]
    rsa = RSA(n, e, d)
    print(f"\nPublic keys: [N: {n}, E: {e}]\nPrivate keys: [N: {n}, D: {d}]\n")
    while should_continue:
        user_input = int(input("Type '1' to encrypt any text, '2' to decrypt ciphertexts: "))
        if user_input == 1:
            plaintext = input("\nType your text to encrypt: ")
            print("\nEncrypting...")
            cipher = rsa.encrypt(plaintext)
            print(f"\nYour text encrypted is:\n{cipher}\n")
        elif user_input == 2:
            ciphertext = input("\nType your text to decrypt: ")
            print("\nDecrypting...")
            cipher = rsa.decrypt(ciphertext)
            print(f"\nYour text decrypted is:\n{cipher}\n")
        else:
            print("\nExiting...")
            should_continue = False

if __name__ == "__main__":
    menu()