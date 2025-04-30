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
