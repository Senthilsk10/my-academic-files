def vigenere_encrypt(plaintext, key):
    plaintext = plaintext.upper().replace(" ", "")
    key = key.upper().replace(" ", "")
    
    ciphertext = ""
    
    for i in range(len(plaintext)):
        p = ord(plaintext[i]) - ord('A')
        k = ord(key[i % len(key)]) - ord('A')
        c = (p + k) % 26
        
        ciphertext += chr(c + ord('A'))
    
    return ciphertext

def vigenere_decrypt(ciphertext, key):
    ciphertext = ciphertext.upper().replace(" ", "")
    key = key.upper().replace(" ", "")
    
    plaintext = ""
    
    
    for i in range(len(ciphertext)):
        c = ord(ciphertext[i]) - ord('A')
        
        k = ord(key[i % len(key)]) - ord('A')
        
        p = (c - k) % 26
        
        plaintext += chr(p + ord('A'))
    
    return plaintext

# Example usage
if __name__ == "__main__":
    message = "ATTACKATDAWN"
    key = "LEMON"
    
    encrypted = vigenere_encrypt(message, key)
    print(f"Original message: {message}")
    print(f"Encrypted message: {encrypted}")
    
    decrypted = vigenere_decrypt(encrypted, key)
    print(f"Decrypted message: {decrypted}")