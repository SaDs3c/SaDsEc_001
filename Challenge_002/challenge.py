import base64
#Definition of variable
authors  = ['hZ3tZb', '3VfYX', 'Zmx', 'fTGVFVH0=', 'JlXzR']
compiller = "mZVlT"

# ANSI escape sequences for colors
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
RESET = '\033[0m'

def header():
    print(GREEN + """
    **********************************************
    *                                            *
    *""" + YELLOW + """    Welcome to the cryptography challenge! """ + GREEN + """ *
    *             H4X0Rz [Challenge]             *
    *             Author: @war_lord              *
    *             Powered by: SaDsEc             *
    **********************************************""" + RESET + """
Decrypt the following encrypted flag to find the solution:
    """)

# Rotate each character in the string by a certain number of positions
def rotate(string, positions):
    rotated = ""
    for char in string:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            rotated += chr((ord(char) - ascii_offset - positions) % 26 + ascii_offset)
        else:
            rotated += char
    return rotated

# Encrypt the string using a rotation cipher with a given key
def encrypt(string, key):
    encrypted = ""
    for char in string:
        encrypted += rotate(char, key)
    return encrypted

# Flag
run_program = sorted(authors, key=lambda x: compiller.index(x[1]) if x[1] in compiller else len(compiller) + 1)
run  = ''.join(run_program)

flag = base64.b64decode(run).decode()

# Challenge header()
header()

# Encrypt the flag multiple times with rotation ciphers
encrypted_flag = encrypt(flag, 5)
encrypted_flag = encrypt(encrypted_flag, 7)
encrypted_flag = encrypt(encrypted_flag, 3)

# Provide the encrypted flag for the challenge
print("Encrypted Flag:", base64.b64encode(encrypted_flag.encode()).decode())
print()

# User input and decryption process
print("Enter your decrypted flag:")

user_input = input().strip()

# Decrypt the user's input (Rotate)
decrypted_flag = rotate(user_input, -3)
decrypted_flag = rotate(decrypted_flag, -7)
decrypted_flag = rotate(decrypted_flag, -5)

# Check if the user's input matches the correct flag
if decrypted_flag == flag:
    print(GREEN + "Congratulations! You solved the challenge!")
    print("The flag is:", decrypted_flag + RESET)
else:
    print(RED + "Sorry, that's not the correct flag." + RESET)
