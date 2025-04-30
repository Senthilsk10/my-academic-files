def prepare_text(text, size):
    text = ''.join(filter(str.isalpha, text.lower()))
    text += 'x' * ((size - len(text) % size) % size)  # Padding if necessary
    print(text)
    return text

def text_to_matrix(text, size):
    out = [[ord(text[i+j]) - ord('a') for j in range(size)] for i in range(0, len(text), size)]
    return out
def matrix_to_text(matrix):
    return ''.join(chr(val % 26 + ord('a')) for row in matrix for val in row)

def mod_inverse(matrix, mod=26):
    det = (matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]) % mod
    inv_det = pow(det, -1, mod) if det else None
    if inv_det is None:
        return None
    
    adjugate = [[matrix[1][1], -matrix[0][1]], [-matrix[1][0], matrix[0][0]]]
    return [[(inv_det * adjugate[i][j]) % mod for j in range(2)] for i in range(2)]

def multiply_matrices(mat1, mat2, mod=26):
    rows, cols = len(mat1), len(mat2[0])
    result = [[sum(mat1[i][k] * mat2[k][j] for k in range(len(mat2))) % mod for j in range(cols)] for i in range(rows)]
    return result

def hill_cipher(text, key, mode="encrypt"):
    size = len(key)
    text = prepare_text(text, size)
    text_matrix = text_to_matrix(text, size)

    key_inv = mod_inverse(key) if mode == "decrypt" else key
    if key_inv is None:
        return "key matrix is not invertible!"

    result_matrix = multiply_matrices(text_matrix, key_inv)
    return matrix_to_text(result_matrix)

# Example usage
key = [[6, 24], [1, 13]]  # 2x2 Key matrix
plaintext = "helloworld"

ciphertext = hill_cipher(plaintext, key, "encrypt")
decrypted_text = hill_cipher(ciphertext, key, "decrypt")

print(f"Ciphertext: {ciphertext}")
print(f"Decrypted text: {decrypted_text}")
