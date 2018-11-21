# DO NOT MODIFY THESE 2 LINES
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
ALPHABET += ALPHABET.upper() + ' .,!?'

def encrypt(msg, shift):

   # Takes string msg and an integer shift returns new string which is an encrypted version of the message

    caesar = ''

    for character in msg:
        i = (ALPHABET.index(character) + shift) % len(ALPHABET)
        caesar += ALPHABET[i]

    return caesar


def decrypt(encrypted_msg, shift):

    #Takes string encrypted_msg and integer shift returns new string which is a decrypted versionof the message

    caesar = ''

    for j in encrypted_msg:
        character = (ALPHABET.index(j) - shift) % len(ALPHABET)
        caesar += ALPHABET[character]

    return caesar

msg = input("Give string: ")

encrypted_msg = encrypt(msg, 10)

print(encrypted_msg)

decrypted_msg = decrypt(encrypted_msg, 10)
print(decrypted_msg)


