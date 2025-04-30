
"""
Hill Cipher Encryption & Decryption (2x2 Matrix Version) - Pseudocode

1. Define Constants:
   - ALPHABET: All capital letters A–Z
   - MOD: 26 (for modulo arithmetic with English alphabet)

2. Helper Functions:
   - char_to_num(c): Convert character to number (A=0, ..., Z=25)
   - num_to_char(n): Convert number back to character using modulo 26
   - mod_inverse(a, m): Find modular inverse of a under modulo m
   - adjoint_2x2(matrix): Return the adjoint (classical adjugate) of a 2x2 matrix
   - inverse_2x2(matrix): Compute inverse of 2x2 matrix under modulo 26
   - chunk_text(text, size): Split text into equal-sized chunks, pad with 'X' if needed

3. Encryption Process (encrypt function):
   - Clean and chunk the plaintext into 2-letter groups
   - For each pair:
     - Convert characters to numbers (vector)
     - Multiply with the key matrix (mod 26)
     - Convert result back to letters
   - Combine all encrypted chunks into final ciphertext

4. Decryption Process (decrypt function):
   - Compute inverse of the key matrix modulo 26
   - Clean and chunk the ciphertext into 2-letter groups
   - For each pair:
     - Convert characters to numbers
     - Multiply with the inverse matrix (mod 26)
     - Convert result back to letters
   - Combine all decrypted chunks into final plaintext

NOTE:
- The key matrix must be invertible under mod 26
- Padding with 'X' ensures complete 2-letter pairs

"""


ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
MOD = 26

def char_to_num(c):
    return ALPHABET.index(c)

def num_to_char(n):
    return ALPHABET[n % MOD]

def mod_inverse(a, m):
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    raise ValueError(f"No mod inverse found for {a} under mod {m}")

def adjoint_2x2(matrix):
    [[a, b], [c, d]] = matrix
    return [[d, -b], [-c, a]]

def inverse_2x2(matrix):
    det = (matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]) % MOD
    det_inv = mod_inverse(det, MOD)
    adj = adjoint_2x2(matrix)
    inv = [[(det_inv * adj[i][j]) % MOD for j in range(2)] for i in range(2)]
    return inv

def chunk_text(text, size):
    text = text.upper().replace(' ', '')
    if len(text) % size != 0:
        text += 'X' * (size - len(text) % size)
    return [text[i:i+size] for i in range(0, len(text), size)]

def encrypt(plain_text, key_matrix):
    chunks = chunk_text(plain_text, 2)
    cipher = ''
    for pair in chunks:
        vec = [char_to_num(c) for c in pair]
        enc_vec = [
            (key_matrix[0][0]*vec[0] + key_matrix[0][1]*vec[1]) % MOD,
            (key_matrix[1][0]*vec[0] + key_matrix[1][1]*vec[1]) % MOD
        ]
        cipher += ''.join(num_to_char(n) for n in enc_vec)
    return cipher

def decrypt(cipher_text, key_matrix):
    inv_key = inverse_2x2(key_matrix)
    chunks = chunk_text(cipher_text, 2)
    plain = ''
    for pair in chunks:
        vec = [char_to_num(c) for c in pair]
        dec_vec = [
            (inv_key[0][0]*vec[0] + inv_key[0][1]*vec[1]) % MOD,
            (inv_key[1][0]*vec[0] + inv_key[1][1]*vec[1]) % MOD
        ]
        plain += ''.join(num_to_char(n) for n in dec_vec)
    return plain

# Example usage
key = [[2, 3], [3, 6]]  # Must be invertible mod 26
message = "attack"

cipher = encrypt(message, key)
print("Encrypted:", cipher)

plain = decrypt(cipher, key)
print("Decrypted:", plain)
