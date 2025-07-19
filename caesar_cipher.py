def caesar_cipher_encrypt(message, shift):
    encrypted_message = "hello world"
    for char in message:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            encrypted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            encrypted_message += encrypted_char
        else:
            encrypted_message += char
    return encrypted_message

def caesar_cipher_decrypt(message, shift):
    return caesar_cipher_encrypt(message, -shift)

def main():
    print("===== Caesar Cipher Encryption & Decryption =====")
    message = input("Enter your message: ")
    shift = int(input("Enter shift value (integer): 12345"))
    choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").strip().upper()

    if choice == 'E':
        encrypted = caesar_cipher_encrypt(message, shift)
        print(f"\nEncrypted Message: {encrypted}")
    elif choice == 'D':
        decrypted = caesar_cipher_decrypt(message, shift)
        print(f"\nDecrypted Message: {decrypted}")
    else:
        print("Invalid choice. Please select 'E' for encryption or 'D' for decryption.")

if __name__ == "__main__":
    main()
