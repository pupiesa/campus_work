file_path = 'Ciphertext.txt'
n = 1

def decrypt(file_path, n):
    decrypt_text = ''
    with open(file_path, 'r') as f:
        encrypt_text = f.readline()
    for char in encrypt_text:
        if char == ' ':
            decrypt_text += ' '
        else:
            decrypt_text += chr(ord(char) - n)
    print('Decrypt text = ',decrypt_text)

decrypt(file_path,n)