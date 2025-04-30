import random

'''
### 🔑 RSA Glossary & Terms
| Term | Description |
|------|-------------|
| **RSA** | Rivest–Shamir–Adleman; a public-key cryptographic algorithm used for secure data transmission. |
| **Public Key** | A key used to **encrypt** messages; shared openly. In RSA, it consists of `(e, n)`. |
| **Private Key** | A key used to **decrypt** messages; kept secret. In RSA, it consists of `(d, n)`. |
| **Plaintext** | The original readable message before encryption. |
| **Ciphertext** | The encrypted, unreadable version of the plaintext. |
| **Encryption** | The process of converting plaintext into ciphertext using the public key. |
| **Decryption** | The process of converting ciphertext back to plaintext using the private key. |
| **p and q** | Two distinct prime numbers chosen during key generation. |
| **n** | The product of `p` and `q` (`n = p × q`); part of both public and private keys. |
| **φ(n)** or **phi(n)** | Euler’s totient function; for RSA, φ(n) = (p−1)(q−1). Used in key generation. |
| **e** | A number such that `1 < e < φ(n)` and `gcd(e, φ(n)) = 1`; used in the public key. |
| **d** | The modular inverse of `e` modulo φ(n); satisfies `(e × d) mod φ(n) = 1`. Used in the private key. |
| **Modular Exponentiation** | Raising a number to an exponent, then taking a modulus (e.g., `a^b mod n`). |
| **GCD (Greatest Common Divisor)** | The largest number that divides two numbers without a remainder. Used to ensure `e` and φ(n) are coprime. |
| **Modular Inverse** | A number `d` such that `(e × d) mod φ(n) = 1`. It helps in computing the private key. |
| **One-Way Function** | A function that is easy to compute but hard to reverse. RSA relies on the difficulty of factoring `n` into `p` and `q`. |

---
'''

"""
steps:
1. Key Generation
   - Choose: p, q (primes)
   - Compute: n = p × q
   - Compute: φ(n) = (p−1)(q−1)
   - Choose: e (1 < e < φ(n), gcd = 1)
   - Find: d ≡ e⁻¹ mod φ(n)
   - Public Key: (e, n)
   - Private Key: (d, n)
2. Encryption
   - Input: M (message)
   - Ciphertext: C = M^e mod n

2. Encryption
   - Input: M (message)
   - Ciphertext: C = M^e mod n

"""

# Step 2: Compute GCD
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Step 3: Find modular inverse
def mod_inverse(e, phi):
    for d in range(1, phi):
        if (e * d) % phi == 1:
            return d
    return None

# Step 4: Key generation
def generate_keys():
    # Use small primes for simplicity
    p = 17
    q = 11
    n = p * q
    phi = (p - 1) * (q - 1)
    print("n",n)
    print("phi",phi)
    # Choose e such that 1 < e < phi and gcd(e, phi) == 1
    e = 3
    while gcd(e, phi) != 1:
        e += 2

    d = mod_inverse(e, phi)
    return (e, n), (d, n)

# Step 5: Encryption
def encrypt(plaintext, public_key):
    e, n = public_key
    encrypted = [(ord(char) ** e) % n for char in plaintext]
    return encrypted

# Step 6: Decryption
def decrypt(ciphertext, private_key):
    d, n = private_key
    decrypted = ''.join([chr((char ** d) % n) for char in ciphertext])
    return decrypted

# === Example Usage ===
public_key, private_key = generate_keys()
print("pub: ",public_key)
print("pri: ",private_key)
message = "hello"
cipher = encrypt(message, public_key)
print("Encrypted:", cipher)

decrypted_message = decrypt(cipher, private_key)
print("Decrypted:", decrypted_message)
