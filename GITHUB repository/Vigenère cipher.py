def remove_special_characters(text):
    result = ""

    for char in text:
        code = ord(char)

        if (0xC0 <= code <= 0xC5) or (0xE0 <= code <= 0xE5):
            char = 'A'

        elif code in (0xC6, 0xE6):
            result += 'AE'

        elif code in (0xC7, 0xE7):
            char = 'C'

        elif (0xC8 <= code <= 0xCB) or (0xE8 <= code <= 0xEB):
            char = 'E'

        elif (0xCC <= code <= 0xCF) or (0xEC <= code <= 0xEF):
            char = 'I'

        elif code == 0xD0:
            char = 'D'

        elif code in (0xD1, 0xF1):
            char = 'N'

        elif (0xD2 <= code <= 0xD6) or (0xF2 <= code <= 0xF6):
            char = 'O'

        elif (0xD9 <= code <= 0xDC) or (0xF9 <= code <= 0xFC):
            char = 'U'

        elif code in (0xDD, 0xFD, 0xFF):
            char = 'Y'

        if ('A' <= char <= 'Z') or ('a' <= char <= 'z') or (char == ' '):
            result += char

    return result


def vigenere_encrypt(text, key):
    result = ""
    key_index = 0
    key = key.upper()

    for letter in text:
        if letter.isalpha():
            text_value = ord(letter)
            value_A = ord('A')

            text_position = text_value - value_A
            key_position = ord(key[key_index % len(key)]) - value_A

            encrypted_position = (text_position + key_position) % 26
            encrypted_letter = chr(encrypted_position + value_A)

            result += encrypted_letter
            key_index += 1
        else:
            result += letter

    return result


file_name = input("Enter the file name: ")
key_input = input("Enter your key (word): ")
key = key_input.upper()

try:
    with open(file_name, "r") as file:
        content = file.read()
        print(content)

    content = content.upper()
    modified_text = remove_special_characters(content)

    result = vigenere_encrypt(modified_text, key)

    print(result)

    choice = input("\nDo you have an output file? (Yes/No): ").lower()

    if choice == "yes":
        output_file = input("What is the file name? : ")
    else:
        output_file = "result.txt"
        print(f"File automatically created: {output_file}")

    with open(output_file, "w") as output:
        output.write(result)
        output.write("\n\n")

        key_index = 0
        for letter, encrypted in zip(modified_text, result):
            if letter.isalpha():
                current_key = key[key_index % len(key)]
                key_index += 1
            else:
                current_key = " "

            output.write(f"{letter} | {current_key} | {encrypted}\n")

    print("Result successfully saved!")

except FileNotFoundError:
    print(f"The file '{file_name}' does not exist. Creating it...")

    with open(file_name, "w") as file:
        print(f"File '{file_name}' created.")
        content = ""  # empty file
