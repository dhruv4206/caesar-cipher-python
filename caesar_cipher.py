def caesar_cipher(text, shift, mode):
    result = ""

    for char in text:
        if char.isalpha():
            # Handle uppercase and lowercase letters
            start = ord('A') if char.isupper() else ord('a')

            # Encrypt or decrypt based on mode
            if mode == "encrypt":
                shifted = (ord(char) - start + shift) % 26
            else:
                shifted = (ord(char) - start - shift) % 26

            result += chr(start + shifted)
        else:
            # Keep spaces and special characters unchanged
            result += char

    return result


# User input
message = input("Enter your message: ")
shift = int(input("Enter shift value: "))

# Encrypt the message
encrypted_message = caesar_cipher(message, shift, "encrypt")
print("\nEncrypted Message:", encrypted_message)

# Decrypt the message
decrypted_message = caesar_cipher(encrypted_message, shift, "decrypt")
print("Decrypted Message:", decrypted_message)
