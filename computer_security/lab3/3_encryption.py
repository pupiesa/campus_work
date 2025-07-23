letter_path = 'letter.txt'
# เลื่อน n ตัวอักษร
n = 1
def encrypt(path,n):
    encrypted = ''
    with open(path, 'r') as f:
        x = f.readline()
        for char in x:
            if char == ' ':
                encrypted += ' '
            else:
                encrypted += chr(ord(char) + n)
        print('Ciphertext = ',encrypted)
        with open('Ciphertext.txt' , 'w') as f:
            f.write(encrypted)
encrypt(letter_path,n)

