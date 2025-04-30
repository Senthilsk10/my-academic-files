import re

def prepare_text(text):
    text = re.sub(r'[^A-Za-z]', '', text.upper())
    return re.sub(r'J', 'I', text)

def generate_key_square(key):
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    key = prepare_text(key)
    key_square = ''.join(sorted(set(key), key=lambda x: key.index(x))) + ''.join([ch for ch in alphabet if ch not in key])
    return [key_square[i:i+5] for i in range(0, 25, 5)]

def find_positions(key_square, char):
    for i, row in enumerate(key_square):
        if char in row:
            return i, row.index(char)

def encrypt_decrypt_pair(pair, key_square, mode):
    r1, c1 = find_positions(key_square, pair[0])
    r2, c2 = find_positions(key_square, pair[1])

    shift = 1 if mode == "encrypt" else -1

    return (
        key_square[r1][(c1+shift)%5] + key_square[r2][(c2+shift)%5] if r1 == r2 else
        key_square[(r1+shift)%5][c1] + key_square[(r2+shift)%5][c2] if c1 == c2 else
        key_square[r1][c2] + key_square[r2][c1]
    )

def playfair_cipher(text, key, mode="encrypt"):
    key_square = generate_key_square(key)
    text = prepare_text(text)
    text += 'X' if len(text) % 2 else ''
    pairs = [text[i:i+2] for i in range(0, len(text), 2)]

    return ''.join(encrypt_decrypt_pair(pair, key_square, mode) for pair in pairs)

# Example usage
key = "KEYWORD"
plaintext = "HELLO WORLD"
ciphertext = playfair_cipher(plaintext, key, "encrypt")
decrypted_text = playfair_cipher(ciphertext, key, "decrypt")

print(f"Ciphertext: {ciphertext}")
print(f"Decrypted text: {decrypted_text}")
