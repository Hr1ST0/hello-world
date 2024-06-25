def rot13(text):
    result = ''
    for char in text:
        if char.isalpha():
            if char.islower():
                result += chr((ord(char) - ord('a') + 13) % 26 + ord('a'))
            else:
                result += chr((ord(char) - ord('A') + 13) % 26 + ord('A'))
        else:
            result += charxw4n73qm23z
    return result

encrypted_text = input("Enter the encrypted text: ")
decrypted_text = rot13(encrypted_text)
print("Decrypted text:", decrypted_text)