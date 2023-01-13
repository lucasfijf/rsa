class RSA:
    
    def __init__(self, n: int, e: int, d: int) -> None:
        self.d = d
        self.e = e
        self.n = n

    def encrypt(self, plaintext: str) -> str:
        cipher = [chr((ord(char) ** self.e) % self.n) for char in plaintext]
        cipher = ''.join(cipher)
        return cipher
    
    def decrypt(self, ciphertext: str) -> str:
        plain = [chr((ord(char) ** self.d) % self.n) for char in ciphertext]
        plain = ''.join(plain)
        return plain