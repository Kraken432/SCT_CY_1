def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                base = ord('A')  # 65
            else:
                base = ord('a')  # 97


            new_char = chr((ord(char) - base + shift) % 26 + base)
            result += new_char
        else:
            result += char
    return result


def decrypt(text, shift):
    return encrypt(text, -shift)


# === Main Program ===
while True:
    print("    Caesar Cipher Menu   ")
    print("    -------------------  ")
    print("1. Encrypt a message")
    print("2. Decrypt a message")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ").strip()

    if choice == '1':
        message = input("Enter your message to encrypt: ")
        try:
            shift = int(input("Enter the shift value (e.g., 3): "))
        except ValueError:
            print("Please enter a valid number for shift!")
            continue
        encrypted = encrypt(message, shift)
        print("Encrypted Message:", encrypted)

    elif choice == '2':
        message = input("Enter your message to decrypt: ")
        try:
            shift = int(input("Enter the shift value used during encryption: "))
        except ValueError:
            print("Please enter a valid number for shift!")
            continue
        decrypted = decrypt(message, shift)
        print("Decrypted Message:", decrypted)

    elif choice == '3':
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please choose 1, 2, or 3.")
