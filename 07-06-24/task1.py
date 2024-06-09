'File Encryption/Decryption Program'
import numpy as np
def encrypt_file(input_file, output_file, key):
    """
    Encrypt a file using Caesar cipher algorithm.

    Parameters
    ----------
    input_file : str
        The name of the input file to be encrypted.
    output_file : str
        The name of the output file to save the encrypted content.
    key : int
        The encryption key for Caesar cipher.

    """
    with open(input_file, 'r',encoding='utf-8') as f:
        text = f.read()

    encrypted_text = ''
    for char in text:
        if char.isalpha():
            shifted = ord(char) + key
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char

    with open(output_file, 'w',encoding='utf-8') as f:
        f.write(encrypted_text)


def decrypt_file(input_file, output_file, key):
    """
    Decrypt a file encrypted with Caesar cipher algorithm.

    Parameters
    ----------
    input_file : str
        The name of the input file to be decrypted.
    output_file : str
        The name of the output file to save the decrypted content.
    key : int
        The decryption key for Caesar cipher (same as encryption key).

    """
    with open(input_file, 'r',encoding='utf-8') as f:
        text = f.read()

    decrypted_text = ''
    for char in text:
        if char.isalpha():
            shifted = ord(char) - key
            if char.islower():
                if shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted < ord('A'):
                    shifted += 26
            decrypted_text += chr(shifted)
        else:
            decrypted_text += char

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(decrypted_text)

def main():
    """
    Main function to run the encryption/decryption program.

    Prompts the user for input and output file names, key, and choice
    to either encrypt or decrypt the file.

    """
    input_file = input("Enter input file path: ")
    output_file = input("Enter output file path: ")
    key = int(input("Enter encryption/decryption key: "))

    choice = input("Enter 'E' to encrypt or 'D' to decrypt: ").upper()

    if choice == 'E':
        encrypt_file(input_file, output_file, key)
        print("File encrypted successfully!")
    elif choice == 'D':
        decrypt_file(input_file, output_file, key)
        print("File decrypted successfully!")
    else:
        print("Invalid choice!")


if __name__ == "__main__":
    main()
