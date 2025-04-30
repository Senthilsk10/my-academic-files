from secrets import SystemRandom


"""
Diffie-Hellman Key Exchange - Pseudocode

1. Agree on common base (g) and prime modulus (p)
   - These values are public and known to both parties

2. Each party chooses a private secret
   - Alice picks A (random)
   - Bob picks B (random)

3. Each party computes their public value
   - Alice computes a = g^A mod p
   - Bob computes b = g^B mod p

4. Exchange public values
   - Alice sends a to Bob
   - Bob sends b to Alice

5. Each party computes the shared secret key
   - Alice computes secret_key = b^A mod p
   - Bob computes secret_key = a^B mod p

6. Both should now have the same shared key
   - secret_key (Alice) == secret_key (Bob)

This shared key can be used for secure communication.
"""


prng = SystemRandom()

g = prng.randint(1, 100)
p = prng.randint(1, 100)
print(f"Agreed g: {g}, p: {p}\n")

A = prng.randint(1, 100)
B = prng.randint(1, 100)
print(f"Alice's private key: {A}, Bob's private key: {B}\n")

a = pow(g, A, p)  # Alice's public value
b = pow(g, B, p)  # Bob's public value
print(f"Alice's public value: {a}, Bob's public value: {b}\n")

secret_key1 = pow(b, A, p)  # Alice's secret key
secret_key2 = pow(a, B, p)  # Bob's secret key

if secret_key1 == secret_key2:
    print(f"Secret key successfully derived: {secret_key1}")
else:
    print("Secret keys don't match. Something went wrong!")
