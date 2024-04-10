# Oskar Dolega 04/09/2024

def encoder(password):
    encoded_password = ""
    for char in str(password):
        char = int(char)
        char += 3
        if char >= 10:
            char -= 10
        encoded_password += str(char)
    return encoded_password

def decode(password):

    decoded_password = ""

    for char in password:
        char = int(char)
        char -= 3

        if char <= -1:
            char += 10

        char = str(char)

        decoded_password += char

    return decoded_password


def main():
    encoded_password = ""

    while True:
        print("""Menu
-------------
1. Encode
2. Decode
3. Quit
""")
        option = input("Please enter an option: ")
        if option == "1":
            password_input = input("Please enter your password to encode: ")
            encoded_password = encoder(password_input)
            print("Your password has been encoded and stored!")

        elif option == "2":
            decoded_password = decode(encoded_password)
            print(f'The encoded password is {encoded_password}, and the original password is {decoded_password}')

        elif option == '3':
            break

        else:
            print("Invalid option, please try again!")

if __name__ == "__main__":
    main()
