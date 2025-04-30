from math import ceil
def encrypt(text):
    encrypted_text = [text[i] for i in range(0, len(text), 2)] + [text[i] for i in range(1, len(text), 2)]
    return "".join(encrypted_text)

def decrypt(text):
    if len(text) % 2 != 0: 
        text += '?'
    i, j = 0, ceil(len(text)/2) 
    decrypted_text = ''
    for k in range(0, ceil(len(text)/2)): 
        decrypted_text += text[i] + text[j]
        i += 1
        j += 1
    return decrypted_text.strip("?")

plaintext = input("Enter text: ") 
cipher_text = encrypt(plaintext)
print("Encrypted text: " + cipher_text) 
print("Decrypted text: " + decrypt(cipher_text))


