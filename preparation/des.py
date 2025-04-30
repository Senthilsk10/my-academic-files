def feistel_round(left, right, key):
    f_output = right ^ key
    new_left = right
    new_right = left ^ f_output
    return new_left, new_right

def encrypt(plain_int, key):
    left = (plain_int >> 8) & 0xFF
    right = plain_int & 0xFF

    left, right = feistel_round(left, right, key)

    return (left << 8) | right

def decrypt(cipher_int, key):
    left = (cipher_int >> 8) & 0xFF
    right = cipher_int & 0xFF

    new_right = left
    new_left = right ^ (left ^ key)

    return (new_left << 8) | new_right

plain_text = "Hello"
plain_int = (ord(plain_text[0]) << 8) | ord(plain_text[1])

key = 0x2A  # example 8-bit key

cipher_int = encrypt(plain_int, key)
decrypted_int = decrypt(cipher_int, key)

# Convert back to characters
dec_left = chr((decrypted_int >> 8) & 0xFF)
dec_right = chr(decrypted_int & 0xFF)

print("Original Text:", plain_text)
print("Encrypted (int):", cipher_int)
print("Decrypted Text:", dec_left + dec_right)
