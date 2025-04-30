#this one is just gcd as short hand recursive function.
def euclid(a, b):
    return a if b == 0 else euclid(b, a % b)

def mod_inverse(a, m):
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x

p, q = 823, 953
n = p * q
phi_n = (p - 1) * (q - 1)

e = 313
if euclid(e, phi_n) != 1:
    raise ValueError("e is not coprime with φ(n). Choose another e.")

d = mod_inverse(e, phi_n)
if d is None:
    raise ValueError("No modular inverse found for e.")

print("Private key (d):", d)

M = 19070
S = pow(M, d, n)  # Signature

M1 = pow(S, e, n)  # Recovered message

if M == M1:
    print("Valid signature. Message accepted.")
else:
    print("Invalid signature. Message rejected.")
